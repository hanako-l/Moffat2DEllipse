class Moffat2DEllipse(Fittable2DModel):
    """
    Two dimensional Moffat model with ellipse
    And I do hope I did this right
    
    Parameters
    ----------
    amplitude : float
        Amplitude of the model.
    x_0 : float
        x position of the maximum of the Moffat model.
    y_0 : float
        y position of the maximum of the Moffat model.
    gamma : float
        Core width of the Moffat model.
    alpha : float
        Power index of the Moffat model.
    phi : float
        The angle of the elliptical.
    q : float
        The proportion of semi-major axis and semi-minor axis.
    
    See Also
    ----------
    Moffat2D
    
    Note
    ----------
    Model formula:
        
    .. math ::
        
        x_prime = (x - x_0) * cos(phi) + (y - y_0) * sin(phi) + x_0
        y_prime = (y - y_0) * cos(phi) - (x - x_0) * sin(phi) + y_0
        ksi = sqrt[ (x_prime - x_0) ** 2 + (y_prime - y_0) ** 2 / q]
        f(x, y) = A * [1 + ksi ** 2 / gamma] ** (- alpha)
    """
    amplitude = Parameter(default = 1)
    x_0 = Parameter(default = 0)
    y_0 = Parameter(default = 0)
    gamma = Parameter(default = 1)
    alpha = Parameter(default = 1)
    phi = Parameter(default = 0)
    q = Parameter(default = 1)
    
    @staticmethod
    def evaluate(x, y, amplitude, x_0, y_0, gamma, alpha, phi, q):
        """Two dimensional Moffat model function with ellipcity"""
        
        x_prime = (x - x_0) * math.cos(phi) + (y - y_0) * math.sin(phi) + x_0
        y_prime = (y - y_0) * math.cos(phi) - (x - x_0) * math.sin(phi) + y_0
        ksi = math.sqrt((x_prime - x_0) ** 2 + (y_prime - y_0) ** 2 / q)
        return amplitude * (1 + ksi ** 2 / gamma) ** (- alpha)
