# Hadoop on Jupyter

- Notebooks to deploy a Hadoop cluster using Docker.
- Hands-on activities using YARN, HDFS, Flume, Sqoop, MapReduce, MRJob, Pig, Hive and Spark.

---

Requisitos do computador

- Suporte a virtualização habilitado na BIOS do computador (Hardware assisted virtualization)

  - Depende da máquina, modelo, processador e placa-mãe
  - Processador Intel - Intel Virtualization Technology (Intel-VT-X)
  - Processador AMD - Secure Virtual Machine Mode (AMD-V)
  - Sites com exemplos
    - https://www.youtube.com/watch?v=rzCe4Tolzgs
    - https://www.youtube.com/watch?v=QTTGA4u7azE
    - https://www.thefastcode.com/pt-eur/article/how-to-enable-intel-vt-x-in-your-computer-s-bios-or-uefi-firmware

- Mínimo de 16GBytes de memória RAM

  

Requisitos usando Linux

- Testado em Ubuntu 18.04 e Ubuntu 20.04
- Instalação dos softwares
  - Docker Engine (https://www.docker.com/)
    - https://docs.docker.com/engine/install/ubuntu/
  - Python 3.6 ou superior
    - Sugestão: usar instalador miniconda (https://docs.conda.io/en/latest/miniconda.html)
    - Alternativa: https://python.org.br/instalacao-linux/
  - Jupyterlab (https://jupyter.org/)
    - https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html
    - https://jupyter.org/install



Requisitos usando Mac OS

- Testado em Big Sur
- Instalação dos softwares
  - Docker Desktop (https://www.docker.com/)
    - https://docs.docker.com/desktop/mac/install/
    - Aumentar recursos disponíveis no Docker para suportar no mínimo containers com 4GB de memória e 2GB de Swap (Preferences -> Resources)
      - https://docs.docker.com/desktop/mac/
  - Python 3.6 ou superior
    - Sugestão: usar instalador miniconda (https://docs.conda.io/en/latest/miniconda.html)
    - Alternativa: https://python.org.br/instalacao-mac/
  - Jupyterlab (https://jupyter.org/)
    - https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html
    - https://jupyter.org/install



Requisitos usando Windows

- Testado em Windows 10
- Habilitar suporte a WSL2
  - https://docs.microsoft.com/pt-br/windows/wsl/install-win10#manual-installation-steps
  - Na etapa 6, instalar o Ubuntu 20.04 LTS
- Instalação dos softwares
  - Docker Desktop (https://www.docker.com/)
    - https://docs.docker.com/desktop/windows/install/
    - Habilitar o suporte a WSL2 (General -> Use the WSL 2 based engine)
    - Habilitar integração com o Ubuntu instalado juntamente com o WSL 2 (Resources -> WSL Integration)
      - https://docs.docker.com/desktop/windows/wsl/
    - https://docs.microsoft.com/pt-br/windows/wsl/tutorials/wsl-containers
    - https://andrewlock.net/installing-docker-desktop-for-windows/
  - Python 3.6 ou superior
    - Sugestão: usar instalador miniconda (https://docs.conda.io/en/latest/miniconda.html)
    - Alternativa: https://python.org.br/instalacao-windows/
  - Jupyterlab (https://jupyter.org/)
    - https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html
    - https://jupyter.org/install
