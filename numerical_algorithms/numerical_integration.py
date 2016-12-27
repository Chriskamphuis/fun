class intergrate:

    def rectangle_rule(self, function, xmin, xmax, num_intervals):
        '''
        Calculates the area under a function using the rectangle rule.
        '''
        dx = (float(xmax) - float(xmin))/num_intervals
        area = 0.0
        x = xmin
        for i in range(num_intervals):
            area += dx * function(x)
            x += dx
        return area

    def trapezoid_rule(self, function, xmin, xmax, num_intervals):
        '''
        Calculates the area under a function using the trapezoid rule.
        '''
        dx = (float(xmax) - float(xmin))/num_intervals
        area = 0.0
        x = xmin
        for i in range(num_intervals):
            area += dx * (function(x) + function(x + dx))/2.0
            x += dx
        return area

    def adaptive_quadrature(self, function, xmin, xmax,
                            num_intervals, max_slice_error):
        '''
        Intergrate using an adaptive midpoint trapezoid rule
        '''
        dx = (float(xmax) - float(xmin))/num_intervals
        area = 0.0
        x = xmin
        for i in range(num_intervals):
            area += self.slice_area(function, x, x + dx, max_slice_error)
            x += dx
        return area

    def slice_area(self, function, x1, x2, max_slice_error):
        '''
        Calculates the area of a slice. If the error is to big the slice gets
        splitted in two new slicex. To which the same procedure
        will be applied to.
        '''
        y1 = function(x1)
        y2 = function(x2)
        xm = (x1 + x2)/2.0
        ym = function(xm)

        area12 = (x2 - x1) * (y1 + y2) / 2.0
        area1m = (xm - x1) * (y1 + ym) / 2.0
        aream2 = (x2 - xm) * (ym + y2) / 2.0
        area1m2 = area1m + aream2

        error = (area1m2 - area12)/area12

        if(abs(error) < max_slice_error):
            return area1m2

        return (self.slice_area(function, x1, xm, max_slice_error) +
                self.slice_area(function, xm, x2, max_slice_error))

    def monte_carlo_integration(self):
        '''
        Calculates the area of a shape using monte_carlo_integration. I am not
        entirely sure yet how I want to represent shapes. If I have thought of
        a good solution to do this I will implement this function.
        '''
        raise NotImplementedError

    def newton_raphson(self, f, dfdx, initial_guess, max_error):
        '''
        Finds a zero of a function using the Newton-Raphson method, which is a
        method similiar to gradient descent. For simple function as for example
        the sine you will find a zero in less than 10 iterations.
        '''
        x = initial_guess
        for i in range(100):
            y = f(x)
            if abs(y) < max_error:
                break
            x = x - y / dfdx(x)
        return x
