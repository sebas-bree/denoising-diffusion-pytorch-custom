from setuptools import setup, find_packages

exec(open('denoising_diffusion_pytorch_custom/version.py').read())

setup(
  name = 'denoising-diffusion-pytorch-custom',
  packages = find_packages(),
  version = __version__,
  license='MIT',
  description = 'Denoising Diffusion Probabilistic Models - Pytorch',
  author = 'Bas Bree',
  author_email = 'sebas.bree@gmail.com',
  url = 'https://github.com/sebas-bree/denoising-diffusion-pytorch-custom',
  long_description_content_type = 'text/markdown',
  keywords = [
    'artificial intelligence',
    'generative models'
  ],
  install_requires=[
    'accelerate',
    'einops',
    'ema-pytorch',
    'numpy',
    'pillow',
    'pytorch-fid',
    'torch',
    'torchvision',
    'tqdm'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
