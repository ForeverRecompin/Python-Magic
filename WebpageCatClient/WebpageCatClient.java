import java.io.*;
import java.net.*;

public class WebpageCatClient {
    /*
      Usage:
      make url=https://www.google.com
     */
    public static void main(String[] args) {
        if (args.length != 1) return;
        try {
            URL webpage = new URL(args[0]);
            URLConnection connection = webpage.openConnection();
            try (InputStream rawInputStream = connection.getInputStream()) {
                InputStream buffer = new BufferedInputStream(rawInputStream);
                Reader reader = new InputStreamReader(buffer);
                int c;
                while ((c = reader.read()) != -1) {
                    System.out.print((char) c);
                }
            }
        } catch (MalformedURLException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
