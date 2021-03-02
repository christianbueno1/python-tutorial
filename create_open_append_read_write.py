# f = open('flowers.txt','r')
# print(f.mode)
# print(f.name)

# f.close()

with open('flowers.txt', 'r') as f:
    # pass
    # f_content = f.read() ##return a string <class 'str'>
    # print(type(f_content))
    # print(f_content, end='')
  
    # f_content = f.readlines() ## return a list, notice the s i readlines
    # print(f_content, end='')
    
    # read one line to before LF
    # f_content = f.readline()
    # print(f_content, end='')

    # f_content = f.readline()
    # print(f_content, end='')
    
    # print('hello')

    #read(100) , 100 characters
    # f_content = f.read(100) ##return a string <class 'str'>
    # print(f_content, end='')
    
    # f_content = f.read(100) ##return a string <class 'str'>
    # print(f_content, end='')
    
    # f_content = f.read(100) ##return a string <class 'str'>
    # print(f_content, end='')

    size_to_read = 10
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='*')
        print(f.tell())
        f_contents = f.read(size_to_read)


    # size_to_read = 10
    # f.seek(10)
    # f_content = f.read(size_to_read) ##return a string <class 'str'>
    # print(f_content, end='')
    # ##move the position, seek
    # f.seek(10)
    # f_content = f.read(size_to_read) ##return a string <class 'str'>
    # print(f_content, end='')

    # write
    # with open('money.txt', 'w') as wf:
    #     wf.write('5 apple $4.5')
    #     wf.seek(0)
    #     wf.write('2 ban')



# try:
#     print(f.closed)
#     print(f.read())
# except ValueError:
#     print('error there, ValueError')

