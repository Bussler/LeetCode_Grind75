#pragma once
#include "Solver_Interface.h"
#include <iostream>

using namespace LeetcodeSolving;
using namespace std;


//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


// M: a sorted linked list, merge the lists sorted into one list
class LinkedListSolver : public SolverInterface<ListNode, ListNode, ListNode> {
public:

  ListNode solve(const ListNode& list1, const ListNode& list2) override {

    return NULL;
  }

  ListNode* solve(ListNode* list1, ListNode* list2) {
    
    if (list1 == nullptr)
        return list2;
    if (list2 == nullptr)
        return list1;

    ListNode* merged_list;

    if (list1->val > list2->val){
        merged_list = list2;
        list2 = list2->next;
    }
    else{
        merged_list = list1;
        list1 = list1->next;
    }

    ListNode* pointer_merged = merged_list;


    // M: merge in elements
    while(list1 != nullptr && list2 != nullptr){
        
        if(list1->val > list2->val){
            pointer_merged->next = list2;
            list2 = list2->next;
        }
        else{
            pointer_merged->next = list1;
            list1 = list1->next;
        }
        pointer_merged = pointer_merged->next;
    } 

    // M: merge in all other elements
    if (list1 != nullptr)
        pointer_merged->next = list1;
    else
        pointer_merged->next = list2;
    
    return merged_list;
  }
};
