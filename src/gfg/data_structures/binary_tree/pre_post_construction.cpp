#include <bits/stdc++.h>
using namespace std;

class Node{
    public:
    int data;
    Node *left;
    Node *right;
};

Node* newNode(int data){
    Node* temp = new Node();
    temp->data = data;
    temp->left = temp->right = NULL;
    return temp;
}

Node* constructTreeUtil(int pre[], int preMirror[], int &preIndex, int start, int end, int size){
    if (preIndex >= size){
        return NULL;
    }
    Node* root = newNode(pre[preIndex]);
    preIndex++;
    if (start == end){
        return root;
    }
    int index;
    for(index=start; index <= end; index++){
        if (pre[preIndex] == preMirror[index]){
            break;
        }
    }
    root->left = constructTreeUtil(pre, preMirror, preIndex, index, end, size);
    root->right = constructTreeUtil(pre, preMirror, preIndex, start, index - 1, size);
    return root;
}

Node* constructTree(int pre[], int preMirror[], int size){
    int preIndex = 0;
    Node* root = constructTreeUtil(pre, preMirror, preIndex, 0, size - 1, size);
    return root;
}

int main(){
    int preOrder[] = {1, 2, 4, 5, 3, 6, 7};
    int preMirror[] = {1, 3, 7, 6, 2, 5, 4};
    int size = sizeof(preOrder) / sizeof(preOrder[0]);
    Node* root = constructTree(preOrder, preMirror, size);
    return 0;
}