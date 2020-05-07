from jinja2 import Environment, PackageLoader, select_autoescape
import time


class GReport:
    def __init__(self, container):
        self.container = container
        self.env = Environment(
            loader=PackageLoader('src'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        self.job_template = self.env.get_template('templete.html')

    def set_time(self, begin_time, end_time):
        self.cost_time = end_time - begin_time
        self.begin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(begin_time))
        self.end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))

    def get_report_html(self):
        t = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        return self.job_template.render(
            begin_time=self.begin_time,
            end_time=self.end_time,
            cost_time=self.cost_time,
            container=self.container
        )
