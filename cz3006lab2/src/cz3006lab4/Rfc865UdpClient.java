package cz3006lab4;
import java.io.*; 
import java.net.*; 

public class Rfc865UdpClient {

	public static void main(String[] args) {
		 //
		 // 1. Open UDP socket
		 //
		 DatagramSocket socket;
		 InetAddress ip;
		 try{
			 ip = InetAddress.getByName("localhost"); //CHANGE IP
		 } catch(UnknownHostException e) {
			 System.out.println("Host exception");
			 ip = null;
		 }
		 byte[] message = "Hi".getBytes();
		 byte[] buffer = new byte[65535]; 
		 try {
			 socket = new DatagramSocket();
		 } catch (SocketException e) {
			 System.out.println("Socket exception");
			 socket = null;
		 }

		 try {
			 //
			 // 2. Send UDP request to server
			 //
			 DatagramPacket request = new DatagramPacket(message,message.length,ip,17); //CHANGE PORT
			 socket.send(request);
			 //
			 // 3. Receive UDP reply from server
			 //
			 DatagramPacket reply = new DatagramPacket(buffer, buffer.length);
			 socket.receive(reply);
			 System.out.println(new String(
			          reply.getData(), 0, reply.getLength()));
		 } catch (IOException e) {
			 System.out.println("IO Exception");
		 }

	}

}
