/**
 * Definition for singly-linked list.
*/
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        int len = lists.length;
        
        // erstelle Queue
        PriorityQueue<ListNode> pQueue;
        // sorte alle Elemente in pQueue durch Comparator 
        pQueue = new PriorityQueue<ListNode>(Comparator.comparingInt(elem -> elem.val));
        // füge alle Elemente von Lists an pQueue
        pQueue.addAll(Arrays.asList(lists));
        
        ListNode head = null;
        ListNode last = null;
        while (! pQueue.isEmpty()) { 
            ListNode current = pQueue.poll();
            if (head == null) { 
                head = last = current;
            } else { 
                last.next = current;
                last = current;
            }
            if (current.next != null) { 
                pQueue.add(current.next);
            }
            
        }
        return head;
    }
}
