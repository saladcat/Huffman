import heapq
from Node import Node
import networkx as nx


class Huffman(object):
    list_all_char = list()
    list_all_node = list()

    encode_table = {}
    root = Node()

    def __init__(self):
        pass

    def init_encode(self, string: str):
        """
        :param  string the string need to encode, such as 'i love you '

        init tree and encode table
        """
        self.list_all_char = list()
        self.list_all_node = list()

        self.encode_table = {}
        self.root = Node()

        self._encode(string)
        self._get_encode_table()
        self._get_encode_tree()

    def decode(self, string: str) -> str:
        """
        :param  string the string need to decode
        :return decode string
        """
        ret_str = ""
        cur_node = self.root
        index = 0
        while index < len(string):
            item = string[index]
            if not cur_node.is_leaf():
                if item is '0':
                    cur_node = cur_node.LHS
                else:
                    cur_node = cur_node.RHS
                index += 1
            else:
                ret_str += cur_node.char
                cur_node = self.root

        ret_str += cur_node.char
        return ret_str

    def _get_encode_table(self):
        """

        :return encode table
        """
        for item in self.list_all_char:
            self.encode_table[item.char] = item.code
        return self.encode_table

    def _get_encode_tree(self):
        """
        :return: G the encode three
        """
        G = nx.DiGraph()
        list_node_name = [item.char for item in self.list_all_node]
        G.add_nodes_from(list_node_name)
        list_node_edge = []
        for item in self.list_all_node:
            if item.LHS is not None:
                tup = (item.char, item.LHS.char, 0)
                list_node_edge.append(tup)
            if item.RHS is not None:
                tup = (item.char, item.RHS.char, 1)
                list_node_edge.append(tup)

        # list_node_left = [(item.char, item.LHS.char, 0) for item in self.list_all_node]
        # list_node_right = [(item.char, item.RHS.char, 1) for item in self.list_all_node]
        fixed_position = {}
        len_bin = [0 for i in range(0, 1000)]

        for item in self.list_all_node:
            pos_x = len(item.code)

            fixed_position[item.char] = (pos_x, len_bin[pos_x])
            len_bin[pos_x] += 1

        G.add_weighted_edges_from(list_node_edge)

        edge_labels = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])
        nx.draw(G, pos=fixed_position, node_color='b', edge_color='r', with_labels=True, font_size=10, node_size=0)

        nx.draw_networkx_edge_labels(G, fixed_position, edge_labels=edge_labels)  # 绘制图中边的权重
        # plt.show()

        return G

    def _encode(self, string: str):
        """
        :param string: init string
        """
        list_str = list(string)
        list_cnt_bin = self._get_cnt_bin(list_str)
        self.list_all_char = list_cnt_bin[:]
        self.list_all_node = list_cnt_bin[:]

        self._switch_pri_queue(list_cnt_bin)
        while len(list_cnt_bin) > 1:
            node1 = heapq.heappop(list_cnt_bin)
            node2 = heapq.heappop(list_cnt_bin)
            cmb_node = Node("-1", node1, node2)
            heapq.heappush(list_cnt_bin, cmb_node)
            self.list_all_node.append(cmb_node)

        last_node = heapq.heappop(list_cnt_bin)
        last_node.code_set("")
        self.root = last_node

    def _get_cnt_bin(self, list_char: list) -> list:
        """
        :param list_char: the list content all char(split string char by char)
        :return: the list content all no repeat char, and the numbers
        """
        list_no_repeat = sorted(list(set(list_char)))
        list_cnt_char = list()
        for item in list_no_repeat:
            list_cnt_char.append(Node(item))

        for item in list_char:
            for char in list_cnt_char:
                if item is char.char:
                    char.increase()
                    break
        return list_cnt_char

    def _switch_pri_queue(self, list_node):
        """
        :param list_node: a list which content all

        make list_node be a priority queue
        """
        heapq.heapify(list_node)


if __name__ == '__main__':
    a = Huffman()
    a.init_encode("1234567890")
    a._get_encode_tree()

    print(a.decode("011100"))
