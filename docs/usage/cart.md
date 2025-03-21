
# Customizing the Cart Page

## Displaying a Free Shipping Message on the Cart Page

**Scenario 1: Cart Does Not Qualify for Free Shipping**

![Not-qualify](../img/not-egilible.jpg){ loading=lazy }

**Scenario 2: Cart Qualifies for Free Shipping**

![qualify](../img/promotion-qualify.jpg){ loading=lazy }

To configure these messages, follow these steps:

1.  Navigate to **Marketing** > **Promotions** and click **Create**. Select **With legacy editor**.
2.  In the **Promotion detail** section, name your promotion.
3.  In the **Promotion type** section, select `Orders totaling more than X amount get free shipping to specific shipping zones`. In the **spend at least** field, enter the minimum order amount required for free shipping.

  ![free-shipping-editor](../img/free-shipping.jpg){ loading=lazy }
4.  In the **Promotion options** section, customize your messages:

  *   **Congratulations Banner Message**: Enter the message to display when the cart qualifies for free shipping.
  *   **Upsell Banner Message**: Enter the message to display when the cart does not qualify. Use the format `[your text] %%condition.remaining%% [your text]` to dynamically display the remaining amount needed to qualify.
5.  Click **Save**.

  ![promotion-message](../img/Promotion-message.jpg){ loading=lazy }
