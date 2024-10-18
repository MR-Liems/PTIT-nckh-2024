# graph_description.txt
# This file contains the graph description in Graphviz format.

### Graph description (using Graphviz format)
graph_code = """
graph TB
    A[Initial Assessment Phase] --> B[Infrastructure Development]
    B --> C[Data Collection & Integration]
    
    %% Infrastructure Development Details
    B --> B1[Cloud Computing Setup]
    B --> B2[Hardware Infrastructure]
    B --> B3[Network Infrastructure]
    
    %% Data Collection & Integration
    C --> C1[Data Sources]
    C --> C2[Data Warehousing]
    C --> C3[Data Lakes]
    
    %% Processing & Analysis
    C --> D[Data Processing & Analysis]
    D --> D1[Batch Processing]
    D --> D2[Real-time Processing]
    D --> D3[Machine Learning Integration]
    
    %% Application Development
    D --> E[Application Development]
    E --> E1[Prototype Development]
    E --> E2[Testing & Validation]
    E --> E3[Deployment]
    
    %% Implementation & Monitoring
    E --> F[Implementation Phase]
    F --> F1[User Training]
    F --> F2[System Integration]
    F --> F3[Performance Monitoring]
    
    %% Continuous Improvement
    F --> G[Optimization & Scaling]
    G --> G1[Performance Optimization]
    G --> G2[Scale Infrastructure]
    G --> G3[Update & Maintain]
    
    %% Feedback Loop
    G --> A
"""

# Save the graph code to a separate text file
with open('graph_description.txt', 'w') as file:
    file.write(graph_code)

# Python code to process the graph and generate the diagram
from graphviz import Source

# Load the graph code from the file
with open('graph_description.txt', 'r') as file:
    graph_code = file.read()

# Create a graph object from the graph description
source = Source(graph_code, format='png')

# Render the graph to a file and display it
output_path = 'infrastructure_data_integration_process_graph'
source.render(output_path, view=False)

# Display the graph image
from PIL import Image

graph_image = Image.open(f'{output_path}.png')
graph_image.show()
