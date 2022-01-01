import bisect

class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        
        taskq = []
        # sort task with available time
        for i in range(len(tasks)):
            task = [tasks[i][0], i]
            pos = bisect.bisect_left(taskq, task)
            taskq.insert(pos, task)
        
        t = 0
        execq = []
        order = []
        while taskq or execq:
            # exec next task
            next_idle_time = 0
            if execq:
                [exec_time, taskId] = execq.pop(0)
                order.append(taskId)
                next_idle_time = t + exec_time
            elif taskq:
                [next_idle_time, _] = taskq[0]
            
            # time span for executing current task
            while t < next_idle_time:
                # schedule task when available
                while taskq and taskq[0][0] <= next_idle_time:
                    [avai_time, taskId] = taskq.pop(0)
                    task = [tasks[taskId][1], taskId]
                    pos = bisect.bisect_left(execq, task)
                    execq.insert(pos, task)
                    t = avai_time
                else:
                    t = next_idle_time
            
        return order
                    
                
            
    
        
