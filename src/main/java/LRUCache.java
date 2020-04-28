package main.java;

import java.util.HashMap;
import java.util.Map;
import org.w3c.dom.Node;
import sun.applet.AppletResourceLoader;

class LRUCache {

    Map<Integer, Node> keys;
    Node head;
    Node tail;
    int MAX_CAPACITY;
    int CURRENT_CAPACITY;


    class Node {
        int key;
        int value;
        Node prev;
        Node next;

        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
        Node() {
        }

        private void  updateValue(int newValue) {
            this.value = newValue;
        }
    }

    public LRUCache(int capacity) {
        MAX_CAPACITY = capacity;
        CURRENT_CAPACITY = 0;
        keys = new HashMap<>(capacity);
    }

    public int get(int key) {
        if (keys.containsKey(key)) {
            Node data = keys.get(key);
            if (data != head) {
                remove(data);
                add(data);
            }
            return data.value;
        }
        return -1;
    }

    public void put(int key, int value) {

        if (keys.containsKey(key)) {
            Node data = keys.get(key);
            data.updateValue(value);
            this.get(key);
        } else {
            if (CURRENT_CAPACITY == MAX_CAPACITY) {
                remove(tail);
                CURRENT_CAPACITY--;
            }
            add(new Node(key, value));
            CURRENT_CAPACITY++;
        }
    }

    private void add(final Node node) {
        if (head == null) {
            head = tail = node;
        }
        else if (head == tail) {
            head = node;
            head.next = tail;
            tail.prev = head;
        } else {
            node.next = head;
            head.prev = node;
            head = node;
        }
        keys.put(node.key, node);

    }

    private void remove(Node node) {
        if (node.next == null && node.prev == null) {
            head = tail = null;
        }
        else if (node.next != null && node.prev != null) {
            Node temp = node.prev;
            temp.next = node.next;
            temp.next.prev = temp;
        }
        else if (node.next == null) {
            Node temp = tail.prev;
            temp.next.prev = null;
            temp.next = null;
            tail = temp;
        }
        else if (node.prev == null) {
            Node temp = head.next;
            temp.prev.next = null;
            temp.prev = null;
            head = temp;
        }
        keys.remove(node.key);
        node = null;
    }
}

class LRUCacheTester {

    public static void main(String[] args) {
//        ["LRUCache","put","put","get","put","get","put","get","get","get"]
//          [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
//        [null,null,null,1,null,-1,null,-1,3,4]

        LRUCache lruCache = null;

//        ["LRUCache","put","put","put","put","get","get"]
//          [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]

        lruCache = new LRUCache(2);
        lruCache.put(2,1);
        lruCache.put(1,1);
        lruCache.put(2,3);
        lruCache.put(4,1);
        System.out.println(lruCache.get(1));
        System.out.println(lruCache.get(2));

//        LRUCache lruCache = new LRUCache(2);
//        lruCache.put(1,1);
//        lruCache.put(2,2);
//        System.out.println(lruCache.get(1));
//        lruCache.put(3,3);
//        System.out.println(lruCache.get(2));
//        lruCache.put(4,4);
//        System.out.println(lruCache.get(1));
//        System.out.println(lruCache.get(3));
//        System.out.println(lruCache.get(4));
//        System.out.println();

//        ["LRUCache","put","put","put","put","get","get"]
//        [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
//        [null,null,null,null,null,-1,3]

//        ["LRUCache","put","put","get","put","put","get"]
//[[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]

//        lruCache = new LRUCache(2);
//        lruCache.displayState();
//        lruCache.put(2,1);
//        lruCache.displayState();
//        lruCache.put(2,2);
//        lruCache.displayState();
//        System.out.println(lruCache.get(2));
//        lruCache.displayState();
//        lruCache.put(1,1);
//        lruCache.displayState();
//        lruCache.put(4,1);
//        lruCache.displayState();
//        System.out.println(lruCache.get(2));
//        lruCache.displayState();


    }

}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */