import threading
import search_at_mc
import search_at_ign


class CrawlingAtMcThread(threading.Thread):
    def __init__(self, thread_id, apps):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.apps = apps

    def run(self):
        print("开始线程：" + str(self.thread_id))
        search_at_mc.search(apps=self.apps)
        print("退出线程：" + str(self.thread_id))


class CrawlingAtMcPerThread(threading.Thread):
    def __init__(self, thread_id, apps):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.apps = apps

    def run(self):
        print("开始线程：" + str(self.thread_id))
        search_at_mc.search_percentage(apps=self.apps)
        print("退出线程：" + str(self.thread_id))


class CrawlingAtIgnThread(threading.Thread):
    def __init__(self, thread_id, apps):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.apps = apps

    def run(self):
        print("开始线程：" + str(self.thread_id))
        search_at_ign.search(apps=self.apps)
        print("退出线程：" + str(self.thread_id))


def tuple_cut(main_tuple, sub_tuple_len):
    lst = []
    for i in range(0, len(main_tuple), sub_tuple_len):
        lst.append((main_tuple[i:i + sub_tuple_len]))
    return lst


def muti_thread_craw_at_mc(apps_lst):
    i = 0
    for apps in apps_lst:
        i = i + 1
        CrawlingAtMcThread(thread_id=i, apps=apps).start()


def muti_thread_craw_at_mc_per(apps_lst):
    i = 0
    for apps in apps_lst:
        i = i + 1
        CrawlingAtMcPerThread(thread_id=i, apps=apps).start()


def muti_thread_craw_at_ign(apps_lst):
    i = 0
    for apps in apps_lst:
        i = i + 1
        CrawlingAtIgnThread(thread_id=i, apps=apps).start()
