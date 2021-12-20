# Name: Madelief Verburg
# Student number: 14125331
"""
compute_tumour.py
* contains compute functions used for the tumour model
"""


def compute_total_cells(model):
    """Compute number of cells present"""
    return len([cell for cell in model.schedule.agents])


def compute_stem_cells(model):
    """"Compute number of stem_cells"""
    return len([cell for cell in model.schedule.agents if cell.status == "stem_cell"])


def compute_transit_amplifying(model):
    """Compute number of transitional dividing cells"""
    return len([cell for cell in model.schedule.agents if cell.status == "transit_amplifying"])


def compute_differentiated(model):
    """Compute number of transitional non-dividing cells"""
    return len([cell for cell in model.schedule.agents if cell.status == "differentiated"])


def compute_stop_status(model):
    """Compute the status of the model """
    return model.stop_status
