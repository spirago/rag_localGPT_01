#syntax=docker/dockerfile:1
# Build as `docker build . -t spirago/rag_localgpt_cuda`
# docker build . -t spirago/rag_localgpt_cuda
# Push to DockerHuB `docker push spirago/rag_localgpt_cuda`
# Run as `docker run -it --gpus=all spirago/rag_localgpt_cuda`, requires Nvidia container toolkit.

FROM nvidia/cuda:11.7.1-runtime-ubuntu22.04
RUN apt-get update && apt-get install -y software-properties-common
RUN apt-get install -y g++-11 make python3 python-is-python3 pip git
RUN apt-get install -y openssh-server
# Installing LLAMA-CPP :
# LocalGPT uses LlamaCpp-Python for GGML (you will need llama-cpp-python <=0.1.76) and GGUF (llama-cpp-python >=0.1.83) models.
RUN --mount=type=cache,target=/root/.cache CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1
RUN git clone git clone -b feature/toms_branch https://github.com/spirago/rag_localgpt_01.git
RUN cd rag_localgpt_01
RUN pip install --timeout 100 -r /rag_localgpt_01/requirements.txt llama-cpp-python==0.1.83
EXPOSE 5111
EXPOSE 5110
RUN chmod +x /rag_localgpt_01/start.sh
CMD ["/rag_localgpt_01/start.sh"]