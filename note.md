# 多线程 vs 多进程
- 进程
    - 多进程数据共享问题
- 线程
    - 一个进程的多个线程间共享数据和运行环境
    - 共享互斥问题
- 全局解释器锁（GIL）
    - Python代码的执行是由python虚拟机进行控制
    - 在主循环中只能够有一个控制线程在执行
    
- Python包
    - thread：有问题，不好用，python3改成了_thread
    - threading: 通行的包
    - 案例01: 顺序执行，耗时比较长
    - 案例02： 改用多线程，缩短总时间，使用_thread
    - 案例03： 多线程，传参数
    
- threading的使用
    - 直接利用threading.Thread生成Thread实例
        1. t = threading.Thread(target=xxx,args=(xxx,))
        2. t.start():启动多线程
        3. t.join():主程序 等待多线程执行完成，在继续执行
        4. 案例04
        5. 案例05： 加入join
        - 守护线程-daemon
            - 如果在程序中将子线程设置成守护现成，则子线程会在主线程结束的时候自动退出
            - 一般认为，守护线程不重要或者不允许离开主线程独立运行
            - 守护线程案例能否有效果跟环境相关
            - 案例06非守护线程
            - 案例07守护线程
        - 线程常用属性
            1. threading模块提供的一些方法：
                - threading.currentThread：返回当前线程变量
                - threading.enumerate:返回一个包含正在运行的线程的list，正在运行的线程指的是线程启动后，结束前的状态
                - threading.activeCount: 返回正在运行的线程数量，效果跟 len(threading.enumerate)相同
            2. Thread实例对象的方法
                - thr.setName: 给线程设置名字
                - thr.getName: 得到线程的名字
                - thr.isAlive(): 返回线程是否活动的。
                - 案例08
    - 直接继承自threading.Thread
        - 直接继承Thread
        - 重写run函数
        - 类实例可以直接运行
        - 案例09
        - 案例10， 工业风案例       
- 共享变量
    - 共享变量：当多个现成同时访问一个变量的时候，会产生共享变量的问题
    - 案例11
    - 解决方法：锁，信号灯
    - 锁（Lock）
        - 是一个标志，表示一个线程在占用一些资源
        - 使用方法: lock=threading.Lock()
            1. 上锁:   lock.acquire()
            2. 使用共享资源
            3. 解锁，释放资源:  lock.release()
        - 案例12
        - 锁类似一个令牌，拥有令牌才可以向下执行
    - 线程安全问题
        - 一个资源对于多线程不用加锁也没有问题，称为线程安全
        - 线程不安全变量类型：list,set,dict
        - 线程安全变量类型：queue
    - 生产者消费者问题
        - 一个模型，可以用来搭建消息队列
        - 案例13
    - 死锁问题，案例14
    - 锁的等待时间，案例15
    - semphore
        - 允许一个资源最多由几个多线程同时使用
        - 案例16
    - threading.Timer
        - 利用多线程，在指定时间后启动一个功能
        - 案例 17
    - 可重入锁
        - 一个锁，可以被一个线程多次申请
        - 主要解决递归调用的时候，需要申请锁的情况
        - 案例18
# 线程替代方案
- subprocess
    - 完全跳过线程，使用进程
    - 是派生进程的主要替代方案
    - python2.4后引入
- multiprocessiong
    - 使用threadiing接口派生，使用子进程
    - 允许为多核或者多cpu派生进程，接口跟threading非常相似
    - python2.6
- concurrent.futures   
    - 新的异步执行模块
    - 任务级别的操作
    - python3.2后引入
# 多进程
- 进程间通讯(InterprocessCommunication, IPC )
- 进程之间无任何共享状态
- 进程的创建
    - 直接生成Process实例对象， 案例19
    - 派生子类， 案例20
- 在os中查看pid，ppid以及他们的关系
    - 案例21
- 生产者消费者模型       
    - JoinableQueue
    - 案例22
    - 队列中哨兵的使用, 案例23
    - 哨兵的改进， 案例24