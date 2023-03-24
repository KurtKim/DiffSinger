import importlib

from utils.hparams import set_hparams, hparams

set_hparams()
hparams['disable_sample_tqdm'] = True

def run_task():
    assert hparams['task_cls'] != ''
    pkg = ".".join(hparams["task_cls"].split(".")[:-1])
    cls_name = hparams["task_cls"].split(".")[-1]
    task_cls = getattr(importlib.import_module(pkg), cls_name)
    task_cls.start()


if __name__ == '__main__':
    run_task()
