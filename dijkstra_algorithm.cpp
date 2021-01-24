// For directed graph
#include <iostream>
#define INF 9999

using namespace std;

int find_min_distance(int distance[], bool visited[], int N) {
    int min_distance = INF, min_index;
    for (int n = 0; n < N; n++) {
        if (visited[n]==false && distance[n] <= min_distance) {
            min_distance = distance[n];
            min_index = n;
        }
    }
    return min_index;
}

int main() {
    int number_of_nodes, source, destination;
    string shortest_path = "SHORTEST PATH: ";

    cout<<"Please enter the total number of nodes: ";
    cin>>number_of_nodes;

    int cost_matrix[number_of_nodes][number_of_nodes];
    int adjacency_matrix[number_of_nodes][number_of_nodes];

    cout<<"Please enter the Cost matrix: \n";
    for (int row = 0; row < number_of_nodes; row++) {
        
        for (int col = 0; col < number_of_nodes; col++) {
            cin>>cost_matrix[row][col];
            
            if (cost_matrix[row][col]==0) {
                cost_matrix[row][col] = INF;
            }
        } 
    }
    
    cout<<"Please enter the Source Vertex: ";
    cin>>source;

    cout<<"Please enter the Destination Vertex: ";
    cin>>destination;

    // Dijkstra's Algorithm
    int distance[number_of_nodes];
    bool visited[number_of_nodes];

    for (int i = 0; i < number_of_nodes; i++) {
        distance[i] = INF;
        visited[i] = false;
    }

    distance[source] = 0;
    for (int node = 1; node < number_of_nodes; node++) {
        int u = find_min_distance(distance, visited, number_of_nodes);
        visited[u] = true;
        shortest_path.append(to_string(u));

        if (node == destination) {
            break;
        }

        for (int v = 0; v < number_of_nodes; v++) {
            distance[v] *= visited[v];
            if (distance[v]==0 && v != source) {
                distance[v] = INF;
            }

            if (!visited[v] && cost_matrix[u][v] && distance[u]+cost_matrix[u][v]<distance[v]) {
                int temp = distance[u] + cost_matrix[u][v];
                distance[v] = distance[u] + cost_matrix[u][v];
            }
        }
    }

    cout<<"*************** RESULTS ***************"<<endl;

    cout<<shortest_path<<endl;
    cout<<"COST FOR SHORTEST PATH: "<<distance[destination]<<endl;
    
    return 0;
}