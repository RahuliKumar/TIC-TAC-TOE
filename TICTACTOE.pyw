from graphics import *
import random
from random import choice
def fun1():
        def isInside(p,rect):
            rectP1 = rect.getP1();
            rectP2 = rect.getP2();
            if(p.getX() >= rectP1.getX() and p.getX() <= rectP2.getX() and 
               p.getY() >= rectP1.getY() and p.getY() <= rectP2.getY()):
                 return True;
            else:
                     return False;
        global c,a101,a202,a,g,d2text
        win = GraphWin("TIC-TAC-TOE",1000,1000);
        win.setBackground(color_rgb(200,150,50))
        t=Text(Point(430,20),'ENTER BOARD LENGTH GREATER THAN 2')
        t.draw(win)
        win.setCoords(0,600,600,0);
        text1=Text(Point(200,25),'BOARD LENGTH:')
        text2=Text(Point(400,25),'WIN LENGTH:')
        entry1=Entry(Point(250,25),2)
        entry2=Entry(Point(440,25),2)
        text1.draw(win),text2.draw(win),entry1.draw(win),entry2.draw(win)
        rect1=Rectangle(Point(160,40),Point(250,55))
        text5=Text(Point(204,48),'COMPUTER')
        rect2=Rectangle(Point(360,40),Point(450,55))
        text5.draw(win)
        text6=Text(Point(405,48),'HUMAN')
        rect3=Rectangle(Point(480,15),Point(570,35))
        text7=Text(Point(525,25),'CLICK TO CONFIRM')
        rect1.draw(win),rect2.draw(win),text6.draw(win),rect3.draw(win),text7.draw(win)
        p=win.getMouse()
        while not(isInside(p,rect3)):
                  p=win.getMouse()
        a=int(entry1.getText())
        g=int(entry2.getText())
        entry1.undraw(),entry2.undraw()
        text3=Text(Point(250,25),str(a))
        text4=Text(Point(440,25),str(g))
        text3.draw(win),text4.draw(win)
        q=win.getMouse()
        if a<3:
                text=Text(Point(300,200),'ENTER BOARD LENGTH GREATER THAN 2,CLICK ANYWHERE TO PLAY IN A NEW WINDOW')
                text.draw(win)
                time.sleep(2)
                win.getMouse()
                win.close()
                return fun1()
        if a<g:
                text=Text(Point(300,200),'ARE U NUTS!,WIN LENGTH SHOULD NOT BE GREATER THAN BOARD LENGTH,CLICK ANYWHERE TO PLAY IN NEW WINDOW')
                text.draw(win)
                win.getMouse()
                win.close()
                return fun1()
        while (not(isInside(q,rect1)) and not(isInside(q,rect2))):
            q=win.getMouse()
        player=0
        if isInside(q,rect1):
            text5.undraw()
            rect1.setFill('Red')
            text5.draw(win)
            player=2
        if isInside(q,rect2):
            rect2.setFill('Red')
            player=1
        i,k,o=0,[],[]#making list for using(a=grid no,i=a counter,k=empty list for rectangle,g=win length,o=list copy)
        b=range(1,a*a+1)
        if player==1:
                d2text = Text(Point(210+4*a,(70+50*(a+1))),'TURN OF X');
                d2text.setSize(14)
                d2text.draw(win);
        while i<a:#display board
            j=0
            while j<a:
                rect=Rectangle(Point(175+50*j,100+50*i),Point(225+50*j,150+50*i));
                k=k+[rect]
                rect.setFill("Green");
                #time.sleep(1)   
                rect.draw(win);
                j=j+1
            i=i+1
        c=Rectangle(Point(175,100),Point(225+50*(j-1),150+50*(i-1)))
        a101,a202=j,i
        for t in k:
            o=o+[t]
        #isExit = False;
        
        
        def diagonal(x,z):#it extract the diagonal containing a number from matrix of z*z 
            l=[]
            while x%z!=0 and x<=z*z-z-1:
                x=x+z+1
            if x%z==0:
                while (x/z)>=0:
                   l,x=l+[x],x-z-1
                return l
            else:
                while x%z>=1:
                     l,x=l+[x],x-z-1
                return l
        def diagonal2(x,z):#same as above but in cross direction
            l=[]
            while x%z!=0 and x-2*(z-1)>=0:
                x=x-z+1
            if x==z*z:
                l=l+[x]
                return l
            if x%z==0:
                while (x/z)<z:
                   l,x=l+[x],x+z-1
                return l
            else:
                while x%z>=1:
                     l,x=l+[x],x+z-1
                return l
        def extract(x,y,z):#it creat list(d) of lists(each of length z) extracting from a given list(x),each sublist contaning a given number(y)
            global g
            d=[]
            k=x.index(y)
            i=k-g+1
            while i<=k:
                if i>=0 and i<=k and len(x)-i>=g:
                            d=d+[x[i:i+z]]
                            i=i+1
                else:
                    i=i+1
            return d
        def check(x,y):#check if all elements are equal in a list for indices presant in list y
                i=1
                temp=x[y[0]-1]
                while i<len(y):
                        if temp==x[y[i]-1]:
                                i=i+1
                        else:
                               return False
                return True
        def anyone(x,y,z):#check for any sublist contaning same elements
                #print x,y,z
                global g
                for i in extract(x,y,z):
                        if check(b,i)==True:
                                
                                return True
                return False
        def horizontal(x):
               w,t=[],x
               while t%a!=0:
                       t=t+1
               w=w+range(t-a+1,t+1)
               w.sort()
               return w
        def vertical(x):
                if x%a!=0:
                        return range(x%a,a*(a-1)+x%a+1,a)
                else:
                        return range(a,a*a+1,a)
        def printforX(i):
                                          line=Line(i.getP1(),i.getP2())
                                          line.setWidth(2)
                                          line.setFill('Red')
                                          line.draw(win)
                                          line1=Line(Point(i.getP1().getX(),i.getP2().getY()),Point(i.getP2().getX(),i.getP1().getY()))
                                          line1.setWidth(2)
                                          line1.setFill('Red')
                                          line1.draw(win)
                                          b[o.index(i)]='X'
                                          w=o.index(i)
                                          k.remove(i)
                                          return ''
        def printforO(j):
                                                    
                                                     w=Point(((j.getP1().getX())+(j.getP2().getX()))/2.0,((j.getP1().getY())+(j.getP2().getY()))/2.0)
                                                     p=Circle(w,20)
                                                     p.setWidth(2)
                                                     p.draw(win)
                                                     k.remove(j)
                                                     return ''
                                                     
        def printforwin(t,x):
                                                #d2text.undraw()
                                                dtext = Text(Point(180,140+50*(a202)),'REPLAY');
                                                dtext.draw(win);
                                                dtext = Text(Point(330,140+50*(a202)),'EXIT')
                                                dtext.setSize(15)
                                                dtext.draw(win);
                                                dtext = Text(Point(185+4*a,(70+50*(a+1))),'RESULT: '+str(x)+' WON');
                                                dtext.setSize(14)
                                                dtext.draw(win);
                                                if player==2:
                                                        if x=='O':
                                                                dtext.undraw()
                                                                dtext = Text(Point(210+4*a,(70+50*(a+1))),'RESULT:COMPUTER WON');
                                                                dtext.draw(win);
                                                        if x=='X':
                                                                dtext.undraw()
                                                                dtext = Text(Point(210+4*a,(70+50*(a+1))),'RESULT:HUMAN WON');
                                                                dtext.draw(win);
                                                c=Rectangle(Point(150,130+50*(a202)),Point(210,150+50*(a202)))
                                                #c.setFill('Red')
                                                c.draw(win)
                                                d=Rectangle(Point(300,130+50*(a202)),Point(360,150+50*(a202)))
                                                #d.setFill('Red')
                                                d.draw(win)
                                                inputP = win.getMouse();
                                                while not(isInside(inputP,d)) and not(isInside(inputP,c)):
                                                 inputP = win.getMouse();
                                                if (isInside(inputP,d)):
                                                        win.close()
                                                        return ''
                                                if (isInside(inputP,c)):
                                                  win.close()
                                                  return fun1()
        def comp(x,y):
            global a1
            for i in extract(diagonal(x,a),x,g):
                a1=[]
                for j in i:
                        a1=a1+[b[j-1]]
                if a1.count(y)==g-1:
                        return 2
                if a1.count(y)>=2:
                        return 1
            for i in extract(diagonal2(x,a),x,g):
                    a1=[]
                    for j in i:
                        a1=a1+[b[j-1]]
                    if a1.count(y)==g-1:
                        return 2
                    if a1.count(y)>=2:
                        return 1
            for i in extract(vertical(x),x,g):
                    a1=[]
                    for j in i:
                        a1=a1+[b[j-1]]
                    
                    if a1.count(y)==g-1:
                        return 2
                    if a1.count(y)>=2:
                        return 1
            for i in extract(vertical(x),x,g):
                    a1=[]
                    for j in i:
                        a1=a1+[b[j-1]]
                    if a1.count(y)==g-1:
                        return 2
                    if a1.count(y)>=2:
                        return 1
            w,t=[],x
            for i in extract(horizontal(x),x,g):
                            a1=[]
                            for j in i:
                                a1=a1+[b[j-1]]
                            if a1.count(y)==g-1:
                                return 2
                            if a1.count(y)>=2:
                                return 1
            return False

        def decide(x):#it checks the win condition
               global b,a,g
               if anyone(diagonal(x,a),x,g):
                       return 1
               if anyone(diagonal2(x,a),x,g):
                       return 1
               if anyone(vertical(x),x,g):
                                return 1
               if anyone(horizontal(x),x,g):#check horizontal line
                        return 1              
               else:
                       return 2
        def common(x,y):
                for i in x:
                        for j in y:
                                if i==j:
                                        return j
                return False
        def commoncheck(x,y):#it checks for a element y in lines common to x
                for i in horizontal(x):
                        if b[i-1]==y:
                                return False
                for k in vertical(x):
                       if b[k-1]==y:
                                
                                return False
                return True
                                                      
        def printfordraw(t):
                                            #d2text.undraw()
                                            dtext = Text(Point(198+4*a,(70+50*(a+1))),'RESULT: ITS A DRAW');
                                            dtext.setSize(14)
                                            dtext.draw(win);
                                            dtext = Text(Point(180,140+50*(a202)),'REPLAY');
                                            dtext.draw(win);
                                            dtext = Text(Point(330,140+50*(a202)),'EXIT')
                                            dtext.setSize(15)
                                            dtext.draw(win);
                                            c=Rectangle(Point(150,130+50*(a202)),Point(210,150+50*(a202)))
                                            #c.setFill('Red')
                                            c.draw(win)
                                            d=Rectangle(Point(300,130+50*(a202)),Point(360,150+50*(a202)))
                                            #d.setFill('Red')
                                            d.draw(win)
                                            inputP = win.getMouse();
                                            while not(isInside(inputP,d)) and not(isInside(inputP,c)):
                                                    inputP = win.getMouse();
                                            if (isInside(inputP,d)):
                                                        win.close()
                                            if (isInside(inputP,c)):
                                                  win.close()
                                                  return fun1()
                                            return ''
                                          
        def fun():
                    global c,a1,a2,a,g,y1,d2text
                    t,l,y1=0,0,0
                    while True:
                        if l<g-1:
                             inputP = win.getMouse();
                             while not(isInside(inputP,c)):
                                inputP = win.getMouse();
                             while True:
                                 q=1
                                 for x in k:
                                     if (isInside(inputP,x)):
                                         q=2
                                 if q==1:
                                     inputP = win.getMouse();
                                 elif q==2:
                                     break
                             v21=0
                             for i in k:
                                if(isInside(inputP,i)):
                                        if t==0:
                                                o1=o.index(i)+1
                                        v21=o.index(i)+1
                                        t=t+1
                                        '''if player==1:
                                                d2text.undraw()
                                                d2text = Text(Point(210+4*a,(70+50*(a+1))),'TURN OF O');
                                                d2text.setSize(14)
                                                d2text.draw(win);'''
                                        print printforX(i)
                             if player==1:
                                 inputP = win.getMouse();
                                 while not(isInside(inputP,c)):
                                    inputP = win.getMouse();
                                 while True:
                                     q=1
                                     for x in k:
                                         if (isInside(inputP,x)):
                                             q=2
                                     if q==1:
                                         inputP = win.getMouse();
                                     elif q==2:
                                         break
                                 v21=0
                                 for j in k:
                                    if(isInside(inputP,j)):
                                            if t==0:
                                                    o1=o.index(j)+1
                                            v21=o.index(j)+1
                                            t,l,w2=t+1,l+1,1
                                            b[v21-1]='O'
##                                            d2text.undraw()
##                                            d2text = Text(Point(210+4*a,(70+50*(a+1))),'TURN OF X');
##                                            d2text.setSize(14)
##                                            d2text.draw(win);
                                            print printforO(j)
                             if player==2:
                                 w2=0
                                 if a==3 and g==3:
                                      i1=0
                                      if t==1:
                                            print b[4]
                                            if type(b[4])==int:
                                                    b[4]='O'
                                                    t,l,w2=t+1,l+1,1
                                                    print printforO(o[4])
                                            else:
                                                    d1=choice([1,3,7,9])
                                                    b[d1-1]='O'
                                                    t,l,w2=t+1,l+1,1
                                                    print printforO(o[d1-1])
                                      else:
                                              if comp(v21,'X')==2:
                                                      for i in a1:
                                                              if type(i)==int:
                                                                      i1=1
                                                                      b[i-1]='O'
                                                                      t,l,w2,y1=t+1,l+1,1,i
                                                                      print printforO(o[i-1])
                                                      if i1==0:
                                                              o1=choice([2,4,6,8])
                                                              b[o1-1]='O'
                                                              t,l,w2,y1=t+1,l+1,1,o1
                                                              print printforO(o[o1-1])
                                     
                                              else:
                                                      a9,a12=common(horizontal(o1),vertical(v21)),common(horizontal(v21),vertical(o1))
                                                      if type(a12)==int and commoncheck(a12,'O')==True:
                                                                    b[a12-1]='O'
                                                                    t,l,w2,y1=t+1,l+1,1,a12
                                                                    print printforO(o[a12-1])
                                                      else:
                                                            b[a9-1]='O'
                                                            t,l,w2,y1=t+1,l+1,1,a9
                                                            print printforO(o[a9-1])
                                 if l==0 and w2==0 and a>3:
                                       while True:
                                                i=choice([2+a,a*a-a-1,a*a-a+1-a+1,2*a-1])
                                                if type(b[i-1])==int:
                                                                        w2=1
                                                                        b[i-1]='O'
                                                                        y1=i
                                                                        print printforO(o[i-1])
                                                                        t,l=t+1,l+1
                                                if w2==1:
                                                        break
                                 if w2==0:
                                        if comp(v21,'X')==1 or comp(v21,'X')==2:
                                                       for i in a1:
                                                                if type(i)==int:
                                                                        w2=1
                                                                        b[i-1]='O'
                                                                        y1=i
                                                                        print printforO(o[i-1])
                                                                        t,l=t+1,l+1
                                                                        break
                                 if w2==0:
                                        while True:
                                                k2=choice(b)
                                                if type(k2)==int:
                                                        w2=1
                                                        b[k2-1]='O'
                                                        y1=k2
                                                        print printforO(o[k2-1])
                                                        t,l=t+1,l+1
                                                        break
                             
                        elif l>=g-1:
                             inputP = win.getMouse();
                             while not(isInside(inputP,c)):
                                inputP = win.getMouse();
                             while True:
                                 q=1
                                 for x in k:
                                     if (isInside(inputP,x)):
                                         q=2
                                 if q==1:
                                     inputP = win.getMouse();
                                 elif q==2:
                                     break
                             for i in k:
                                if(isInside(inputP,i)):
                                          v21=o.index(i)+1
                                          '''if player==1:
                                                  d2text.undraw()
                                                  d2text = Text(Point(210+4*a,(70+50*(a+1))),'TURN OF O');
                                                  d2text.setSize(14)
                                                  d2text.draw(win);'''
                                          print printforX(i)
                                          t=t+1
                                          v=o.index(i)
                                          if decide(v+1)==1:
                                              print printforwin(t,'X')
                                          if t==a*a:
                                              print printfordraw(t)
                             if t<a*a:
                                    if player==2:
                                            s1=0
                                            if comp(y1,'O')==2:
                                                           for i in a1:
                                                                                if type(i)==int:
                                                                                     b[i-1]='O'
                                                                                     s1=1
                                                                                     print printforO(o[i-1]) 
                                                                                     t,l=t+1,l+1
                                                                                     if decide(y1)==1:
                                                                                        print printforwin(t,'O')
                                                                                     if t==a*a:
                                                                                              print printfordraw(t)
                                            if s1==0:
                                                       if comp(v21,'X')==2 or comp(v21,'X')==1:
                                                                    for i in a1:
                                                                            if type(i)==int:
                                                                                     s1=1
                                                                                     b[i-1]='O'
                                                                                     y1=i
                                                                                     print printforO(o[i-1])
                                                                                     t,l=t+1,l+1
                                                                                     if decide(y1)==1:
                                                                                        print printforwin(t,'O')
                                                                                        return ''
                                                                                     if t==a*a:
                                                                                      print printfordraw(t)
                                                                                     break
                                                                   
                                            if s1==0:
                                                       while True:
                                                                    a6=choice(b)
                                                                    if type(a6)==int:
                                                                                    b[a6-1]='O'
                                                                                    s1,y1=1,a6
                                                                                    print printforO(o[a6-1])
                                                                                    t,l=t+1,l+1
                                                                                    if decide(y1)==1:
                                                                                       print printforwin(t,'O')
                                                                                    if t==a*a:
                                                                                      print printfordraw(t)
                                                                    if s1==1:
                                                                            break
                                    else:
                                             inputP = win.getMouse();
                                             while not(isInside(inputP,c)):
                                                inputP = win.getMouse();
                                             while True:
                                                 q=1
                                                 for x in k:
                                                     if (isInside(inputP,x)):
                                                         q=2
                                                 if q==1:
                                                     inputP = win.getMouse();
                                                 elif q==2:
                                                     break
                                             for j in k:
                                                if(isInside(inputP,j)):
                                                          v21=o.index(j)+1
                                                          '''d2text.undraw()
                                                          d2text = Text(Point(210+4*a,(70+50*(a+1))),'TURN OF X');
                                                          d2text.setSize(14)
                                                          d2text.draw(win);'''
                                                          print printforO(j)
                                                          t,l=t+1,l+1
                                                          v=o.index(j)
                                                          b[v]='O'
                                                          if decide(v+1)==1:
                                                              print printforwin(t,'O')
                                                          if t==a*a:
                                                              print printfordraw(t)  
        print fun()
print fun1()            
                                                     
                                                         


                    
                    
                 
                                    
                 
                     
                      
                      
          
