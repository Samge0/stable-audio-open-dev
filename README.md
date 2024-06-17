# using Stable-audio-open-1.0 with Vscode plugin `Dev Containers`

### NOTICE
You can find Stable-audio-open-1.0：[Stable-audio-open-1.0](https://github.com/Stability-AI/stable-audio-tools)

Model address：[Stable-audio-open-1.0 (huggingface)](https://huggingface.co/stabilityai/stable-audio-open-1.0)  

### How to use 
- copy and customize configuration:
    ```shell
    cp .devcontainer/docker-compose-dev.yml .devcontainer/docker-compose.yml
    ```
- Install the `Dev Containers` plugin for vscode
- shortcut key 'Ctrl+Shift+P' to open the command panel, select `Remote-Containers: Reopen in Container`
- automatically build the container and wait for completion to access the workspace inside the container
- run
    ```shell
    python main.py
    ```

[click here to show more>>](.devcontainer/README.md)

### result

- prompt = "upbeat and rhythmic electronic dance music with a catchy melody and strong bassline"
  
https://github.com/Samge0/stable-audio-open-dev/assets/17336101/8aa266ad-929d-44ae-8834-d10983221476

![image](https://github.com/Samge0/stable-audio-open-dev/assets/17336101/69ef1f87-ed16-468e-8c2b-8e0128870f2e)
