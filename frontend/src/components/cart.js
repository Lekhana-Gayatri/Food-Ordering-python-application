import React, { useEffect, useState } from 'react';
import { getRestaurants, addToCart, removeFromCart } from './api'; // Assuming you have these functions in your api file

const OrderSummary = (props) => {
    const [items, setItems] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        async function fetchData() {
            try {
                const data = await getRestaurants(props.token, props.API_URL);
                setItems(data);
            } catch (error) {
                console.error('Error fetching the cart items:', error);
                setError('Failed to load items. Please try again later.');
            }
        }
        fetchData();
    }, [props.token, props.API_URL]);

    const updateQuantity = async (dishId, newQuantity, price) => {
        try {
            if (newQuantity > 0) {
                await addToCart(props.token, props.API_URL, dishId, newQuantity);
            } else {
                await removeFromCart(props.token, props.API_URL, dishId);
            }
            const updatedItems = items.map(item => 
                item.id === dishId ? { ...item, quantity: newQuantity, total_price: newQuantity * price } : item
            );
            setItems(updatedItems);
        } catch (error) {
            console.error('Error updating the cart:', error);
            setError('Failed to update the cart. Please try again later.');
        }
    };

    // Calculate the total price of all items
    const grandTotal = items.reduce((acc, item) => acc + item.total_price, 0);

    if (items.length === 0) {
        return <div className="empty-cart-message">No Items in CART</div>;
    }

    return (
        <><div class="text-center">
        <h3><i>CART</i></h3>
    </div>
    
        {items.map((res) => (
                <div key={res.id} className="order-card p-5 m-8 border rounded">
                    <div className="d-flex justify-content-between align-items-center mb-3">
                        <div>
                            <h5 className="mb-0">{res.restaurant_name }</h5>
                            <small className="text-muted">{res.location }</small>
                        </div>
                        
                    </div>

                    <div className="order-item mb-3">
                        <div className="d-flex align-items-center">
                            <h6><span>{res.dish_name}</span></h6>
                        </div>
                        <div className="d-flex align-items-center">
                            <button 
                                className="btn btn-outline-secondary btn-sm" 
                                onClick={() => updateQuantity(res.id, res.quantity - 1, res.price)}
                            >
                                -
                            </button>
                            <span className="mx-2">{res.quantity || 1}</span>
                            <button 
                                className="btn btn-outline-secondary btn-sm" 
                                onClick={() => updateQuantity(res.id, res.quantity + 1, res.price)}
                            >
                                +
                            </button>
                            <span className="ms-3 text-muted">₹{res.price}</span>
                        </div>
                    </div>

                    <div className="d-flex justify-content-between">
                        <span>Item Total</span>
                        <span>₹{res.total_price}</span>
                    </div>
                </div>
            ))}
            
            {/* Display the total sum at the bottom */}
            <div className="border-top pt-3 mt-3">
            <div className="d-flex justify-content-between">
                    <strong>Delivery PartnerFee</strong>
                    <strong>₹8</strong>
                </div>
                <div className="d-flex justify-content-between">
                    <strong>Grand Total</strong>
                    <strong>₹{grandTotal+8}</strong>
                </div>
            </div>
        </>
    );
};

export default OrderSummary;
