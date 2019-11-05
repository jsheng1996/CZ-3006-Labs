package cz3006lab4;
import java.io.*; 
import java.net.*; 

public class Rfc865UdpServer {

	public static void main(String[] args) {
		 //
		 // 1. Open UDP socket at well-known port
		 //
		 DatagramSocket socket;
		 byte[] quote = "Quote of the day".getBytes();
		 InetAddress ip;
		 try {
			 socket = new DatagramSocket(17);
		 } catch (SocketException e) {
			 System.out.println("Socket exception");
			 socket = null;
		 }
		 
		 byte[] receive = new byte[65535];
		 DatagramPacket request = null;
		 
		 while (true) {
			 try {
				 //
				 // 2. Listen for UDP request from client
				 //
				 request = new DatagramPacket(receive, receive.length);
				 socket.receive(request);
				 ip =request.getAddress();
				 //
				 // 3. Send UDP reply to client
				 //
				 DatagramPacket reply = new DatagramPacket(quote,quote.length,request.getAddress(),request.getPort());
				 if(new String(
						 request.getData(), 0, request.getLength()).equals("Hi")) {
					 System.out.println("Message received");
					 socket.send(reply);
				 }
			 } catch (IOException e) {}
		 }
	}

}
