
/* Creating node structure*/
class Node{
    int data;
    Node left,right;

    Node(int data)
    {
        this.data=data;
        left=null;
        right=null;
    }
}


/* BST class for operation on tree*/
class BST{
 
 
    /*method for traversing tree in INORDER*/
    void inorder(Node root)
    {
        if(root!=null)
        {
            inorder(root.left);
            System.out.print(root.data+" ");
            inorder(root.right);
        }
    }


/*Method which prints the sum of all leaf values which are smaller than root value*/
    int sum=0;
    int sumOfAllLeafNode(Node root,int rootvalue)
    {
        if(root!=null)
        {
            sumOfAllLeafNode(root.left,rootvalue);
            sumOfAllLeafNode(root.right,rootvalue);
            if(root.data<rootvalue && root.left==null && root.right==null)
            sum=sum + root.data;
                
        }
        return sum;
    }


/* Main method*/
    public static void main (String[] args) {

        BST tmp=new BST();
        int addition=0;
        Node root=new Node(8);
        root.left=new Node(3);
        root.left.left=new Node(1);
        root.left.right=new Node(6);
        root.left.right.left=new Node(4);
        root.left.right.right=new Node(7);
        root.right=new Node(10);
        root.right.right=new Node(14);
        root.right.right.left=new Node(13);
        System.out.println("The INORDER of given tree is:");
        tmp.inorder(root);
        addition=tmp.sumOfAllLeafNode(root,root.data);
        System.out.println("");
         System.out.println("Sum of all leaf values which are smaller than root value is: "+addition);
        
    }
}