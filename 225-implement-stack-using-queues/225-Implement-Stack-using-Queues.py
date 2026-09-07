typedef struct {
   int data[200];
    int front;
    int rear;
    int size; 
} MyStack;

bool myStackEmpty(MyStack* obj) {
    if(obj->size==0)
    {
        return true;
    }
    else
    {
        return false;
    }

}
MyStack* myStackCreate() {
    MyStack* obj=(MyStack*)malloc(sizeof(MyStack));
    obj->front=0;
    obj->rear=-1;
    obj->size=0;
    return obj;
}

void myStackPush(MyStack* obj, int x) {
    if(obj->size>=200)
    {
        return;
    }
    int s=obj->size;
    obj->rear=(obj->rear+1)%200;
    obj->data[obj->rear]=x;
    obj->size++;
     for (int i = 0; i <s; i++) {
        int temp = obj->data[obj->front];
        obj->front = (obj->front + 1) % 200;
        obj->size--;
        obj->rear = (obj->rear + 1) % 200;
        obj->data[obj->rear] = temp;
        obj->size++;
    }
}

int myStackPop(MyStack* obj) {
    if(myStackEmpty(obj))
    {
        return -1;
    }
    int v=obj->data[obj->front];
    obj->front=(obj->front+1)%200;
    obj->size--;
    return v;
}

int myStackTop(MyStack* obj) {
    if(myStackEmpty(obj))
    {
        return -1;
    }
    return obj->data[obj->front];
}
void myStackFree(MyStack* obj) {
    free(obj);
}

/**
 * Your MyStack struct will be instantiated and called as such:
 * MyStack* obj = myStackCreate();
 * myStackPush(obj, x);
 
 * int param_2 = myStackPop(obj);
 
 * int param_3 = myStackTop(obj);
 
 * bool param_4 = myStackEmpty(obj);
 
 * myStackFree(obj);
*/