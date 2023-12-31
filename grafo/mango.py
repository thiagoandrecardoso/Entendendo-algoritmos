from collections import deque

search_queue = deque()

g_mango = {
    "i": ["alice", "bob", "claire"],
    "alice": ["peggy"],
    "bob": ["anuj", "peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

sells_mango = {"peggy": True}

search_queue += g_mango["i"]

verify = []


def sell_mango(person):
    if sells_mango.get(person):
        return sells_mango[person]


def search_mango(queue):
    while queue:
        person = queue.popleft()
        if person not in verify:
            if sell_mango(person):
                print(person + " sells mango!")
                return True
            else:
                queue += g_mango[person]
                verify.append(person)
    return False


search_mango(search_queue)
