# �⺻ �����ڵ�� ���� �����ص� ���� �����ϴ�. ��, ����� ���� ����
# �Ʒ� ǥ�� ����� ���� �ʿ�� �����ϼ���.

# ǥ�� �Է� ����
'''
a = int(input())                        ������ ���� 1�� �Է� �޴� ����
b, c = map(int, input().split())        ������ ���� 2�� �Է� �޴� ���� 
d = float(input())                      �Ǽ��� ���� 1�� �Է� �޴� ����
e, f, g = map(float, input().split())   �Ǽ��� ���� 3�� �Է� �޴� ����
h = input()                             ���ڿ� ���� 1�� �Է� �޴� ����
'''

# ǥ�� ��� ����
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                ������ ���� 1�� ����ϴ� ����
print(b, end = " ")                     �ٹٲ� ���� �ʰ� ������ ������ ������ ����ϴ� ����
print(c, d, e)                          �Ǽ��� ���� 3�� ����ϴ� ����
print(f)                                ���ڿ� 1�� ����ϴ� ����
'''




'''
�Ʒ��� ������ input.txt �� read only �������� �� ��,
������ ǥ�� �Է�(Ű����) ��� input.txt ���Ϸκ��� �о���ڴٴ� �ǹ��� �ڵ��Դϴ�.
�������� �ۼ��� �ڵ带 �׽�Ʈ �� ��, ���Ǹ� ���ؼ� input.txt�� �Է��� ������ ��,
�Ʒ� ������ �̿��ϸ� ���� �Է��� ������ �� ǥ�� �Է� ��� ���Ϸκ��� �Է��� �޾ƿ� �� �ֽ��ϴ�.
���� �׽�Ʈ�� ������ ������ �Ʒ� �ּ��� ����� �� ������ ����ϼŵ� �����ϴ�.
�Ʒ� ������ ����ϱ� ���ؼ��� import sys�� �ʿ��մϴ�.
��, ä���� ���� �ڵ带 �����Ͻ� ������ �ݵ�� �Ʒ� ������ ����ų� �ּ� ó�� �ϼž� �մϴ�.
'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# �������� �׽�Ʈ ���̽��� �־����Ƿ�, ������ ó���մϴ�.
for test_case in range(1, T + 1):
    sudoku = [list(map(int,input().split())) for _ in range(9)]

    count = 0

    #���ο� Ȯ��
    row_sum = 0
    for i in range(9):
        for j in range(9):
            row_sum += sudoku[i][j]
        if row_sum==45:
            count+=1
            row_sum = 0
        else:
            row_sum = 0
    
    #���ο� Ȯ��
    col_sum = 0
    for j in range(9):
        for i in range(9):
            col_sum += sudoku[i][j]
        if col_sum == 45:
            count +=1
            col_sum = 0
        else:
            col_sum = 0
    
    #�簢�� Ȯ��
    rect_sum = 0
    i = 0
    j = 0
    for _ in range(3):
        for _ in range(3):      
            for i in range(3):
                for j in range(3):
                    rect_sum += sudoku[i][j]
            if rect_sum == 45:
            	count +=1
            	rect_sum = 0
            else:
            	rect_sum = 0
            i +=3
        j += 3
        i = 0
        
    if count == 27:
        print('#'+str(test_case)+' '+str(1))
    else:
        print('#'+str(test_case)+' '+str(0))