import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;

public class CarCollection {
    static class Car {
        private final String modelName;
        private final double price;

        Car(String modelName, double price) {
            this.modelName = modelName;
            this.price = price;
        }

        @Override
        public boolean equals(Object object) {
            if (this == object) return true;
            if (!(object instanceof Car)) return false;
            Car other = (Car) object;
            return Double.compare(price, other.price) == 0
                    && modelName.equalsIgnoreCase(other.modelName);
        }

        @Override
        public int hashCode() {
            return Objects.hash(modelName.toLowerCase(), price);
        }
    }

    private final Set<Car> cars = new HashSet<>();

    public void addCar(String modelName, double price) {
        cars.add(new Car(modelName, price));
    }

    public List<String> getHighestPricedCarNames() {
        double highestPrice = cars.stream()
                .mapToDouble(car -> car.price)
                .max()
                .orElseThrow(() -> new IllegalStateException("No cars available"));

        return cars.stream()
                .filter(car -> Double.compare(car.price, highestPrice) == 0)
                .map(car -> car.modelName)
                .sorted(Comparator.naturalOrder())
                .toList();
    }

    public int getCarCount() {
        return cars.size();
    }
}
