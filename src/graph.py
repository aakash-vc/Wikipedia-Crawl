import pandas as pd

class Graph:

    def __init__(self):
        pass

    def get_nodes(self, df):
        labels = pd.concat([df['From'], df['To']])
        labels = labels.unique()
        
        nodes = pd.DataFrame(columns=['ID', 'Nodes', 'Label'])
        nodes['ID'] = range(1, 1+len(labels))
        nodes['Nodes'] = range(1, 1+len(labels))
        nodes['Label'] = labels

        #nodes.to_csv('nodes.csv', index=False)
        #display(nodes)
        return nodes

    def get_edges(self, df, node_df):
        edges = pd.DataFrame()
        edges['Source'] = df['From'].map(node_df.set_index('Label')['Nodes'].to_dict())
        edges['Target'] = df['To'].map(node_df.set_index('Label')['Nodes'].to_dict())
        #print(df)
        
        #edges = df[['Source', 'Target']]
        edges['Type'] = 'Directed'
        edges['Weight'] = 1

        return edges


    def graph(self):
        main_df = pd.read_csv('data/connections.csv')
        nodes_df = self.get_nodes(main_df)
        nodes_df.to_csv('data/nodes.csv', index=False)

        edges_df = self.get_edges(main_df, nodes_df)
        edges_df.to_csv('data/edges.csv', index=False)