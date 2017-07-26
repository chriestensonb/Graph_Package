import Graph_main
import sys

if __name__ == '__main__':
    call_log = open('C:\\Users\\Administrator\\PycharmProjects\\Graphs\\Logs\\call_log.txt','w')
    if len(sys.argv) > 0:
        for i in range(len(sys.argv)):
            call_log.write('Argument ' + str(i) + ': ' + sys.argv[i]+'\n')
    else:
        call_log.write('No Inputs Specified')
    call_log.close()
    num_graphs = int(sys.argv[1])
    num_vertices = int(sys.argv[2])
    num_edges = int(sys.argv[3])
    make_hist = int(sys.argv[4])
    graphs_log = open('C:\\users\\administrator\\PycharmProjects\\Graphs\\Logs\\graph_' +
                      str(num_graphs) + '_' + str(num_vertices) + '_' + str(num_edges) + '.txt','w')
    betti_nums = Graph_main.Main(num_graphs, num_vertices, num_edges,make_hist)
    graphs_log.write('First Betti Number\n')
    for i in range(len(betti_nums.b[0])):
        graphs_log.write(str(betti_nums.b[0][i])+'\n')
    graphs_log.close()
