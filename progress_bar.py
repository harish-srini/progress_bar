import sys
import time

def is_jupyter_notebook():
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter Notebook or JupyterLab
        else:
            return False  # Other IPython shell
    except NameError:
        return False      # Probably standard Python interpreter

def get_total_length(iterable, total):
    if total is not None:
        return total
    try:
        return len(iterable)
    except TypeError:
        return None

def progress_bar(iterable, total=None, length=40, title='Progress'):
    total = get_total_length(iterable, total)
    
    if is_jupyter_notebook():
        from ipywidgets import FloatProgress, VBox, HTML
        from IPython.display import display
        progress_bar_widget = FloatProgress(min=0, max=total or 1)
        percentage_html = HTML()
        elapsed_time_html = HTML()
        title_html = HTML(value=title)
        box = VBox(children=[title_html, progress_bar_widget, percentage_html, elapsed_time_html])
        display(box)

        start_time = time.time()
        for i, item in enumerate(iterable, 1):
            yield item
            progress_bar_widget.value = i
            percentage_html.value = f'<p>{title}: {i}/{total} ({progress_bar_widget.value / (total or 1) * 100:.1f}%)</p>'
            elapsed_time_html.value = f'<p>Elapsed Time: {time.time() - start_time:.2f}s</p>'

    else:
        progress = 0
        start_time = time.time()

        for i, item in enumerate(iterable, 1):
            yield item
            progress = i / total if total is not None and total > 0 else 0
            bar = '=' * int(length * progress) + '-' * (length - int(length * progress))
            elapsed_time = time.time() - start_time
            sys.stdout.write(f'\r{title}: [{bar}] {progress * 100:.1f}% ({i}/{total}) Elapsed Time: {elapsed_time:.2f}s')
            sys.stdout.flush()

        sys.stdout.write('\n')
        sys.stdout.flush()

# Example usage:
data = range(100)
for _ in progress_bar(data, title='Processing'):
    # Your processing logic here
    time.sleep(0.1)  # Simulating some processing time
