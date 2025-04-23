#!/usr/bin/env python

import hydra
import logging
import numpy as np
import sys


@hydra.main(version_base=None, config_path='conf/', config_name='config')
def gen_rand(cfg):
    logger = logging.getLogger(__name__)
    if cfg.n <= 0:
        logger.error(f'negative number to generate {cfg.n}')
        sys.exit(1)
    logger.info(f'generating {cfg.n} random numbers')
    logger.info(f'using {cfg.distr.name} distribution')
    if cfg.distr.name == 'gauss':
        logger.info(f'mu={cfg.distr.mu}, sigma={cfg.distr.sigma}')
        if cfg.distr.sigma <= 0:
            logger.error(f'negative standard deviation {cfg.distr.sigma}')
            sys.exit(1)
        numbers = np.random.normal(loc=cfg.distr.mu, scale=cfg.distr.sigma,
                                   size=(cfg.n,))
    elif cfg.distr.name == 'uniform':
        logger.info(f'a={cfg.distr.a}, b={cfg.distr.b}')
        if cfg.distr.a >= cfg.distr.b:
            logger.warning(f'lower bound exceed upper bound, '
                        f'{cfg.distr.a} >= {cfg.distr.b}')
        numbers = np.random.uniform(cfg.distr.a, cfg.distr.b, size=(cfg.n,))
    logger.info('starting output')
    out = open(cfg.file, 'w') if cfg.file else sys.stdout
    for number in numbers:
        print(number, file=out)
    logger.info('output done')
    return 0

if __name__ == '__main__':
    gen_rand()
