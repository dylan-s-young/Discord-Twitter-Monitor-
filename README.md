<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://static.integromat.com/img/templates/2972.png" alt="Logo" width="110" height="60">
  </a>
    
  <h3 align="center">Discord Twitter Monitor</h3>
    
  <p align="center">
    <a href="https://github.com/GoldenTBE/Discord-Twitter-Monitor-"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/GoldenTBE/Discord-Twitter-Monitor-/issues">Report Bug</a>
    ·
    <a href="https://github.com/GoldenTBE/Discord-Twitter-Monitor-/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#Executing">Executing</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


Monitor a Twitter user using this script! New Tweets are sent to a webhook.


### Built With


* [Python](https://www.python.org/)
* [Tweepy](https://www.tweepy.org/)
* [Discord-Webhook](https://github.com/lovvskillz/python-discord-webhook)



<!-- GETTING STARTED -->
## Getting Started

Follow directions below to use this script.

### Prerequisites

You will need to install the tweepy module. You can achieve that with a simple pip request.
* pip
  ```sh
  pip install tweepy
  ```
You will also need to setup a Discord Webhook and install the discord-webhook module. 
* [Discord Webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
* pip
  ```sh
  pip install discord-webhook
  ```

### Executing

1. Register a free API Key at [twitter.com](https://twitter.com)
2. Clone the repo
   ```sh
   git clone https://github.com/GoldenTBE/Discord-Twitter-Monitor-.git
   ```
3. Enter you webhook details in `twitter_monitor.py`
   ```sh
   webhook_list = ['Your webhook here']
   ```
4. Enter your API in `twitter_details.py`
   ```py
   api_keys = ['API KEY HERE','API SECRET KEY HERE'] auth_keys = ['ACCESS TOKEN HERE','ACESS TOKEN SECRET HERE']
   ```
5. Run `Main.py`
   ```
   Type in the user you want monitored. 
   ```



<!-- USAGE EXAMPLES -->
## Usage

Will Update(12/25/20)



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/GoldenTBE/Discord-Twitter-Monitor-/issues) for a list of proposed features (and known issues).

Update Log - [Update Log](https://github.com/GoldenTBE/Discord-Twitter-Monitor-/blob/master/update_log.md)

```Additions in the Futures```
  ``` 
  - Lower Delay 
  - Proxy Support
  - Multi-user Monitoring
  ```
<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Dylan Young - [Linkedin](https://www.linkedin.com/in/dylan-young-1a565a1b7/) - dylan.s.young@uconn.edu

Project Link: [https://github.com/GoldenTBE/Discord-Twitter-Monitor-](https://github.com/GoldenTBE/Discord-Twitter-Monitor-)


<!-- Acknowledgments -->
## Acknowledgments 

* [README Template](https://github.com/othneildrew/Best-README-Template/edit/master/README.md)
* [Python-discord-Webhook](https://github.com/lovvskillz/python-discord-webhook)