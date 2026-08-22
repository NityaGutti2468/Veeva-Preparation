import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class InventorySystem {
    static class Product {
        private final int productId;
        private final String productCode;
        private final String name;
        private final String category;
        private final double price;

        Product(int productId, String productCode, String name, String category, double price) {
            this.productId = productId;
            this.productCode = productCode;
            this.name = name;
            this.category = category;
            this.price = price;
        }
    }

    private final Map<Integer, List<Product>> productsById = new HashMap<>();
    private final Map<String, List<Product>> productsByCategory = new HashMap<>();

    public void addProduct(Product product) {
        productsById.computeIfAbsent(product.productId, ignored -> new ArrayList<>()).add(product);
        productsByCategory.computeIfAbsent(product.category, ignored -> new ArrayList<>()).add(product);
    }

    public List<Product> getProductsByCategory(String category) {
        return new ArrayList<>(productsByCategory.getOrDefault(category, List.of()));
    }

    public Product getHighestPricedProduct(String category) {
        return getProductsByCategory(category).stream()
                .max(Comparator.comparingDouble(product -> product.price))
                .orElse(null);
    }

    public List<Product> getProductsSortedByPrice(String category) {
        List<Product> products = getProductsByCategory(category);
        products.sort(Comparator.comparingDouble((Product product) -> product.price).reversed());
        return products;
    }
}
