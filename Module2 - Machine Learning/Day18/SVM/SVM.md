- **Support Vector Machines (SVMs)** are machine learning algorithms used for classification and regression purposes.
- One of the powerful machine learning algorithms for classification, regression and outlier detection purposes.
- Builds a model that assigns ==new data points== to one of the given categories.
	- Can be viewed as a ==non-probabilistic== binary linear classifier.
	- Can be used for linear classification purposes.
- Can also efficiently perform a non-linear classification using the **kernel trick**.
	- Enables to ==implicitly map== the inputs into ==high dimensional== feature spaces.
- Fits the widest possible margin between the classes.
	- This is called **large margin classifier**.
	- The decision boundary is determined by the ==edge instances==, which are called **support vectors**.
- # Key Concepts
	- ![image.png](../assets/image_1761732646763_0.png){:height 246, :width 340}
	- **Hyperplane**
		- A decision boundary that ==separates== data points of different classes.
		- The SVM finds the ==maximum== margin hyperplane, which ensures the ==widest separation== between classes.
		- For N dimensional space, the hyperplane has (N - 1) dimensions.
	- **Support Vectors**
		- The ==closest data points== to the hyperplane.
		- They define the hyperplane and ==influence== the margin.
	- **Margin**
		- The ==perpendicular distance== between the hyperplane and the support vectors.
		- SVM maximizes this margin to achieve the best separation.
	- ## Objective
		- Hyperplane Selection
		  logseq.order-list-type:: number
			- SVM identifies ==hyperplanes== that segregate the classes.
			- The goal is to find the ==best hyperplane== with the largest separation (margin) between classes.
		- Maximizing the Margin
		  logseq.order-list-type:: number
			- The optimal hyperplane ensures the ==maximum distance== from the support vectors on both sides.
			- This hyperplane is called the **maximum margin hyperplane**, and the classifier it defines is the **maximum margin classifier**.
		- ![image.png](../assets/image_1761734232970_0.png){:height 169, :width 389}
	- ## Maximal Margin Classifier
		- All instances must be off the decision boundary.
			- Must be on the correct side.
		- Only works for linearly separable data.
		- Highly sensitive to outliers.
			- Often not suitable for real world data.
		- ![image.png](../assets/image_1761780957981_0.png){:height 226, :width 345}
	- ## Soft Margin Classifier
		- Makes model more flexible.
		- Limits the margin violation.
			- Instances inside margin or wrong class.
		- ![image.png](../assets/image_1761780974788_0.png){:height 232, :width 345}
- # SVM tuning parameters
	- ## Kernel trick
		- SVM applies the kernel trick to transform the input space into a higher-dimensional space.
		- This transformation (e.g., from 2D to 3D) makes it possible to separate data points linearly in the new space.
		- Kernel functions systematically find support vector classifier in higher dimensions.
		- Does not actually transform the data.
			- Find the similarity of points through some function.
			- Instead of finding f(x1, y1) and f(x2,y2) the points (x1, y1) and (x2, y2) are taken and the output similarities are computed using a function f(x, y); where f can be any function on x, y.
			- Gaussian function is used to find similarity.
		- ![image.png](../assets/image_1761734956481_0.png){:height 181, :width 183} ![image.png](../assets/image_1761734963793_0.png){:height 190, :width 295}
			- Here, the RBF(Radial Basis Function) of x and y is used.
				- $RBF=\sqrt{X^2+Y^2}$
		- Different SVM algorithms use different SVM kernels:
		  Polynomial
		  Linear
		  Non- Linear 
		  RBF (Radial Basis Function )
		  Sigmoid etc.
			- ***Polynomial Kernel***
				- Computes the relationships between pair of observations.
				- Very popular in Natural Language Processing.
				- The equation of the kernel:
				  $$K(x_{i},x_{j})=(\gamma(x_{i}\cdot x_{j})+r)^{d},\gamma>0$$
				  Where \gamma = scaling factor that represents the linearity of the model, 
				   x_{i}, x_{j}  = input points
				  r = degree of coefficient,
				  d = degree of polynomial.
				- ![image.png](../assets/image_1761735121334_0.png)
			- ***RBF***
				- Finds support vector classifiers in infinite dimensions.
				- The closest observations have a lot of influence than the further ones on the classification of the new observation.
				- The equation:
				  $$\exp\left({-\gamma\left(x_{i}-x_{j}\right)^2}\right)$$
		- For further optimisation the **Gram Matrix** is used.
			- It is a matrix which can be easily stored and manipulated in the memory and is highly efficient to use.
	- ## Regularization
		- Soft margin allows some ==misclassification errors== in the training data to balance between margin maximization and classification accuracy.
		- The ==amount of tolerance== for the misclassification is controlled by a parameter called the **Regularization hyperparameter**, *C*.
		- Determines how much ==weight== should be given to minimizing classification errors versus maximizing the margin.
		- A ==high value== of C means the model is harder in nature (less tolerant to misclassifications).
			- Prone to overfitting.
		- A ==low value== of C means that the model is softer in nature (more tolerant to misclassifications).
			- Less risk of overfitting.
			- Too much reduction → underfitting.
		- C controls the ==Bias/Variance trade-off==.
			- A low bias means that the model has ==low or no assumptions== about the data → soft margin classifier.
			- A high variance means that the model will change depending on what we ==take as training data== → hard margin classifier.
		- C = 1:
		  ![image.png](../assets/image_1761735358608_0.png){:height 161, :width 256} 
		  C = 100:
		  ![image.png](../assets/image_1761735348967_0.png){:height 166, :width 283}
- # Training process
	- Determining a decision boundary that best separates the classes.
	- The loss function (*hinge loss*) tunes the parameters so that the ==margin is maximized==.
	  $$c\left(x,y,f\left(x\right)\right)=\begin{cases}0 & \text{if }y*f(x)\ge1\\ 1-y*f(x) & else\end{cases}$$
		- The cost is 0 if the predicted value and the actual value are of the same sign.
		- If they are not, the loss value is calculated.
	- A **regularization parameter** is also added to the loss function.
		- Enforces smoother, simpler models by penalizing large weight magnitudes.
		- After adding, the cost functions look like:
		  $$\min_{w}\lambda\Vert w\Vert^2+\sum_{i=1}^{n}\left(1-y_{i}\left(x_{i},w\right)\right)_{+}$$
			- In many SVM formulations, $\lambda=\frac{1}{C}$
			- Large λ → stronger regularization → smoother (softer) margin.
			- Small λ → weaker regularization → tighter (harder) margin.
		- If there is no misclassification, only the gradient from the regularization parameter is updated.
		  $$w=w-\alpha\left(2\lambda w\right)$$
		- In case of misclassification, loss is added with the regularization parameter to perform gradient update.
		  $$w=w+\alpha\left(y_{i}\cdot x_{i}-2\lambda w\right)$$
- # SVM regression
	- **Support Vector Regression (SVR)** is a machine learning algorithm used for regression analysis.
	- Different from traditional linear regression methods.
		- It finds a hyperplane that best fits the data points in a continuous space, instead of fitting a line to the data points.
	-
- # Pros and Cons
	- ## Pros
		- Effective in High Dimensions
		- Robust to Overfitting
		- Versatile Kernel Trick
		- Clear Margin of Separation
		- Memory Efficient
	- ## Cons
		- Complexity with Large Datasets: Training time can be high with large datasets, making it less suitable for very large datasets.
		- Choice of Kernel: Selecting the right kernel and tuning the parameters can be challenging and requires domain knowledge.
		- Less Effective with Noisy Data: Performance can degrade with overlapping classes and noisy data.
		- Interpretability: The model can be less interpretable compared to simpler algorithms like logistic regression.
		- Binary Classification: SVM is inherently a binary classifier.
