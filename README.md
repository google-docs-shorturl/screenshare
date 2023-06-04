# Screenshare using Network Sockets in Python

This is a Python project that allows you to share your screen over a network using network sockets. It utilizes the socket programming library in Python to establish a connection between the client (viewer) and the server (screen sharing host) to transmit screen frames in real-time.

## Features

- Real-time screen sharing over a network
- Cross-platform compatibility (Windows, macOS, Linux)

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/google-docs-shorturl/screenshare.git
   ```

2. Change to the project directory:

   ```shell
   cd screenshare
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

Always make sure to run client.py first.

### Client (Screen-sharing Viewer)

1. Run the client script:

   ```shell
   python client.py
   ```

2. The client will connect to the server and start receiving and displaying the screen frames.

### Server (Screen-sharing host)

1. Run the server script:

   ```shell
   python server.py
   ```

2. The client will start running and display the IP address.

If you are unsure of the IP address of the client, run client.py and it will show you.

## Customization

- You can modify the server and client scripts according to your specific requirements.
- The server script (`server.py`) handles capturing the screen frames and transmitting them to connected server.
- The client script (`client.py`) receives the screen frames and displays them.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the functionality of this project, please submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

This project is provided as-is, without any warranty or guarantee of any kind. Use it at your own risk.

## Credits

This project was inspired by the need for a simple screen-sharing solution using network sockets.
