from collections import defaultdict, deque

inp = input('Введите строку для кодирования: ')

def encode_string(inp_string, code_dict):
    ret_list = []

    for symbol in inp_string:
        ret_list.append(code_dict[symbol])

    return ''.join(map(str, ret_list))

class Node:
    def __init__(self, symbol, freq, left=None, right=None):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right
        # if right:
        #     print(f'new node with left {left.freq} and right {right.freq}')

def make_encode_dict(tree, encode_dict, code):
    # print(f'woring with node {tree.symbol=} {tree.left=} {tree.right=}')
    if tree.symbol != '':
        encode_dict[tree.symbol] = code
    if tree.left:
        make_encode_dict(tree.left, encode_dict, code + '0')
    if tree.right:
        make_encode_dict(tree.right, encode_dict, code + '1')



def insert_node_in_deque(dq, node):
    if len(dq) == 0:
        dq.append(node)
        return

    pos = 0
    while node.freq > dq[pos].freq:
        pos = pos + 1
        if pos == len(dq):
            break
    # print(f'Add el {node.freq} at {pos=}')
    dq.insert(pos, node)


letters_dict = defaultdict(int)
for letter in inp:
    letters_dict[letter] += 1

symbols_queue = deque()
# print(len(symbols_queue))
for sym, freque in letters_dict.items():
    new_node = Node(sym, freque)
    insert_node_in_deque(symbols_queue, new_node)
# print(letters_dict)

while len(symbols_queue) > 1:
    el1 = symbols_queue.popleft()
    el2 = symbols_queue.popleft()
    insert_node_in_deque(symbols_queue, Node('', el1.freq + el2.freq, el1, el2))
    # for item in symbols_queue:
    #     print(item.symbol, ':', item.freq, ' <-> ', end='')
    # print()

coding_dict = defaultdict(str)

encoding_tree = symbols_queue.pop()
# print(encoding_tree.left.left.left, encoding_tree.right.right)
make_encode_dict(encoding_tree, coding_dict, '')
print(coding_dict)

print(f'Encoded string: {encode_string(inp, coding_dict)}')
