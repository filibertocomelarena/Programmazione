#n, m =input().split()
#n = int(n)
#m=  int(m)
#if m != 3*n:
    #print('stop!, il numero inserito per m, deve essere 3 volte n!')

#pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
#print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))


#print([('.|.'*(2*i+1)).center(m, '-')for i in range(n//2)])



print(('m').center(7,'p')) #center() parte da una stringa di rifetimento, e gli assegna una posizione centrale
#in una larghezza (7) ceh è il primo parametro,con un simbolo che andrà a riempire questa larghezza ('p')
