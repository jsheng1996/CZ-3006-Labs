# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:30:06 2019

@author: phuaj
"""
'''TODO
1. Add column headers
2. Optional stuff
'''
import pandas as pd
import networkx as nx

df= pd.read_csv('test_SFlow_data.csv', index_col=False,names=['type','flow_agent_addr',
'inputPort','outputPort','src_MAC','dst_MAC','eth_type','in_vlan','out_vlan',
'src_IP','dst_IP','IP_Protocol','ip_tos','ip_ttl','src_port','dst_port',
'tcp_flags','packet_size','IP_size','sampling_rate'])

print('Parsing data...\n')

top5_talkers_ip = df['src_IP'].value_counts()[:5]
top5_listeners_ip = df['dst_IP'].value_counts()[:5]

tcp_count = df['IP_Protocol'].value_counts().get(6)
udp_count = df['IP_Protocol'].value_counts().get(17)
top3_IP_Protocols = df['IP_Protocol'].value_counts()[:3]

top5_apps_protocol = top3_IP_Protocols = df['IP_Protocol'].value_counts()[:5]

total_traffic = df['IP_size'].sum()

print('Top 5 Talkers (IP):')
print(top5_talkers_ip)
print('\n')
   
print('Top 5 Listeners (IP):')
print(top5_listeners_ip)
print('\n')

print('Top 5 Application Protocols:')
print(top5_apps_protocol)
print('\n')

print('Total traffic: {} bytes\n'.format(total_traffic))

print('Additional stats:\n')

pairs={}
for index, row in df.iterrows():
    word1 = row['src_IP']+'/'+row['dst_IP']
    word2 = row['dst_IP']+'/'+row['src_IP']
    if word1 in pairs.keys():
        pairs[word1]+=1
    elif word2 in pairs.keys():
        pairs[word2]+=1
    else:
        pairs[word1]=1

pairs_sorted = sorted([(k,v) for k,v in pairs.items()], key= lambda x: x[1], reverse=True)

print('Top 5 communication pairs:\n{}\n'.format(pairs_sorted[:5]))

G = nx.Graph()
nodes = list(set(df['src_IP'].tolist()+df['dst_IP'].tolist())) #creating nodes
G.add_nodes_from(nodes)
for (p,n) in pairs_sorted:
    G.add_edge(p.split('/')[0], p.split('/')[1], weight=n)
color = []
size = []
for node in nodes:
    if G.degree(node, weight='weight')<25:
        color.append('g')
        size.append(50)
    elif G.degree(node, weight='weight')<50:
        color.append('b')
        size.append(100)
    elif G.degree(node, weight='weight')<75:
        color.append('c')
        size.append(150)
    elif G.degree(node, weight='weight')<100:
        color.append('y')
        size.append(200)
    elif G.degree(node, weight='weight')<125:
        color.append('m')
        size.append(250)
    else:
        color.append('r')
        size.append(300)
edges = G.edges()
weights = [G[u][v]['weight']/10 for u,v in edges]
print('Network visualised:\n')
nx.draw_random(G, node_size=size, node_color=color, width=weights)


