import java.util.Comparator;
import java.util.PriorityQueue;

public class LoadBalancer {
    static class Server {
        final int serverId;
        int activeConnections;

        Server(int serverId) {
            this.serverId = serverId;
        }
    }

    private final PriorityQueue<Server> availableServers = new PriorityQueue<>(
            Comparator.comparingInt((Server server) -> server.activeConnections)
                    .thenComparingInt(server -> server.serverId));

    public LoadBalancer(int serverCount) {
        for (int id = 1; id <= serverCount; id++) {
            availableServers.offer(new Server(id));
        }
    }

    public int allocateRequest() {
        Server server = availableServers.poll();
        server.activeConnections++;
        availableServers.offer(server);
        return server.serverId;
    }
}
