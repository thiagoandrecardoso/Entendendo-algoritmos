from collections import deque

search_queue = deque()

g_mango = {"i": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "claire": ["thom", "jonny"], "anuj": [],
           "peggy": [], "thom": [], "jonny": []}
sells_mango = {"anuj": True}

search_queue += g_mango["i"]


def sell_mango(person):
    return sells_mango[person]


def search_mango(queue):
    while queue:
        person = queue.popleft()
        if sell_mango(person):
            print(person + " sells mango!")
            return True
        else:
            queue += g_mango[person]
    return False
