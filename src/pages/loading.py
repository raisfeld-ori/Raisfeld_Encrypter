from gui.loading import Ui_Form
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QTimer, QThread, pyqtSignal
from typing import Callable, Optional


class Loading(Ui_Form, QWidget):
    task_ended = pyqtSignal(str)
    close_task = pyqtSignal()

    def __init__(self,
                 parent: QWidget | None,
                 next_window: QWidget | None,
                 action: str,
                 time: int,
                 task: Callable[[pyqtSignal, Optional[pyqtSignal]], ...],
                 task_len: int,
                 include_close: bool,
                 initial_task: str):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.next_window = next_window
        self.time = time
        if include_close:
            self.task = TaskRunner(task, self.task_ended, self.close_task)
        else:
            self.task = TaskRunner(task, self.task_ended, None)
        self.current_time = 0
        self.tasks_done = 0
        self.all_tasks = task_len

        self.progressBar.setMaximum(self.all_tasks)
        self.Task.setText(action)
        self.Estimation.setText(f"estimated time: {self.int_to_time(time)}")
        self.progressBar.setValue(0)
        self.TimeLeft.setText("")
        self.Current.setText("")
        self.Task.setText("")

        self.run_tasks()
        self.task_ended.connect(self.task_done)
        self.close_task.connect(self.previous_page)
        self.task_done(initial_task)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    @staticmethod
    def int_to_time(time: int) -> str:
        if time >= 3600:
            return f"{time / 3600} hours"
        elif time >= 60:
            return f"{time / 60} minutes"
        else:
            return f"{time} seconds"

    def update_time(self):
        self.current_time += 1
        self.TimeLeft.setText(self.int_to_time(self.current_time))

    def task_done(self, next_task: str):
        self.tasks_done += 1
        if self.tasks_done == self.all_tasks:
            self.progressBar.setValue(self.tasks_done)
            self.Current.setText("finished all tasks, closing window")
            self.Tasks.setText(f"{self.tasks_done} out of {self.all_tasks}")
            self.close()
        else:
            self.progressBar.setValue(self.tasks_done)
            self.Current.setText(f"currently: {next_task}")
            self.Tasks.setText(f"{self.tasks_done} out of {self.all_tasks}")

    def previous_page(self):
        self.next_window = None
        self.close()

    def closeEvent(self, a0):
        if self.tasks_done != self.all_tasks:
            self.parent.show()
            self.close()

        self.timer.stop()
        self.task.quit()
        if self.next_window:
            self.next_window.show()
            self.next_window.showMaximized()
        self.close()

    def run_tasks(self): self.task.start()


class TaskRunner(QThread):
    def __init__(self, task: Callable[[pyqtSignal,
                                       Optional[pyqtSignal]], ...],
                 task_signal: pyqtSignal,
                 end_task: Optional[pyqtSignal]):
        super().__init__()
        self.task = task
        self.signal = task_signal
        self.end_task = end_task

    def run(self): self.task(self.signal, self.end_task)
