from collections import deque

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


def sell_mango(person):
    if sells_mango.get(person):
        return sells_mango[person]


def search(name):
    search_queue = deque()
    search_queue += g_mango[name]
    verified = []
    while search_queue:
        person = search_queue.popleft()
        if person not in verified:
            if sell_mango(person):
                print(person + " sells mango!")
                return True
            else:
                search_queue += g_mango[person]
                verified.append(person)
    return False


search("i")


