from django.shortcuts import render
from kycverification.models import KYC
from location.models import CustomerLocation, ServiceProviderLocation

# Create your views here.


from math import radians, sin, cos, sqrt, atan2
import heapq

# Haversine formula to calculate distance between two coordinates
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in km
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    return R * c

# Dijkstra's algorithm to find the nearest service providers
def dijkstra_algorithm(customer_location, service_providers):
    graph = {}
    
    # Build the graph with distance calculations
    for provider in service_providers:
        dist = haversine_distance(
            customer_location.latitude, customer_location.longitude, 
            provider.latitude, provider.longitude
        )
        graph[(provider.latitude, provider.longitude)] = (provider, dist)

    # Priority queue for finding shortest path
    pq = [(0, (customer_location.latitude, customer_location.longitude))]
    visited = set()
    distances = {}

    while pq:
        current_distance, current_location = heapq.heappop(pq)

        if current_location in visited:
            continue

        visited.add(current_location)
        distances[current_location] = current_distance

        for neighbor, (provider, weight) in graph.items():
            if neighbor not in visited:
                heapq.heappush(pq, (current_distance + weight, neighbor))

    # Sort by distance and return sorted service providers
    sorted_providers = sorted(
        graph.values(), key=lambda x: distances.get((x[0].latitude, x[0].longitude), float('inf'))
    )
    
    return sorted_providers

def search_service_providers(request):
    service_type = request.GET.get('service_type')
    customer = request.user.customer
    customer_location = CustomerLocation.objects.get(customer=customer)

    # Fetch verified and online service providers of requested type
    service_providers = ServiceProviderLocation.objects.filter(
    service_provider__user__kyc__service_type=service_type,
    service_provider__user__kyc__is_verified=True,
    is_online=True
)
    # Apply Dijkstra's algorithm to find nearest providers
    sorted_providers = dijkstra_algorithm(customer_location, service_providers)

    context = {
        'customer_location': customer_location,
        'service_providers': [provider[0] for provider in sorted_providers[:5]],  # Get top 5 nearest
        'service_type': service_type
    }
    print(service_providers)
    return render(request, 'search_results.html', context)

