#!/usr/bin/env python

from omegaconf import DictConfig, OmegaConf
import hydra

@hydra.main(version_base=None, config_path='conf/', config_name='config')
def my_app(cfg):
    print(OmegaConf.to_yaml(cfg))

if __name__ == '__main__':
    my_app()
