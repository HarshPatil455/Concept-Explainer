import math

def ohms_law(voltage=None, current=None, resistance=None):
    if voltage is None:
        return current * resistance, "V = I × R"
    elif current is None:
        return voltage / resistance, "I = V / R"
    elif resistance is None:
        return voltage / current, "R = V / I"
    else:
        return None, "Provide only two known values."

def kinetic_energy(mass, velocity):
    ke = 0.5 * mass * velocity**2
    return ke, "KE = 0.5 × m × v²"

def projectile_range(velocity, angle_deg):
    angle_rad = math.radians(angle_deg)
    range_ = (velocity**2 * math.sin(2 * angle_rad)) / 9.8
    return range_, "R = v² × sin(2θ) / g"

def newtons_second_law(mass, acceleration):
    force = mass * acceleration
    return force, "F = m × a"

def ideal_gas_law(pressure=None, volume=None, moles=None, temperature=None, R=8.314):
    if pressure is None:
        return (moles * R * temperature) / volume, "P = nRT / V"
    elif volume is None:
        return (moles * R * temperature) / pressure, "V = nRT / P"
    elif moles is None:
        return (pressure * volume) / (R * temperature), "n = PV / RT"
    elif temperature is None:
        return (pressure * volume) / (moles * R), "T = PV / nR"
    else:
        return None, "Provide only three known values."

def stress(force, area):
    return force / area, "Stress = Force / Area"

def strain(change_in_length, original_length):
    return change_in_length / original_length, "Strain = ΔL / L"

def electrical_power(voltage=None, current=None, resistance=None):
    if voltage is not None and current is not None:
        return voltage * current, "P = V × I"
    elif current is not None and resistance is not None:
        return current**2 * resistance, "P = I² × R"
    elif voltage is not None and resistance is not None:
        return (voltage**2) / resistance, "P = V² / R"
    else:
        return None, "Provide two known values."

def work_done(force, distance):
    return force * distance, "Work = Force × Distance"

def efficiency(output_energy, input_energy):
    return (output_energy / input_energy) * 100, "Efficiency = (Output / Input) × 100%"

def bernoulli(p1, v1, h1, p2, v2, h2, rho=1000, g=9.8):
    lhs = p1 + 0.5 * rho * v1**2 + rho * g * h1
    rhs = p2 + 0.5 * rho * v2**2 + rho * g * h2
    return abs(lhs - rhs), "Bernoulli: P₁ + ½ρv₁² + ρgh₁ = P₂ + ½ρv₂² + ρgh₂"
