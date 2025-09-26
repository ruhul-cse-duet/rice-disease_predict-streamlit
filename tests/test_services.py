"""
Tests for service components
"""
import pytest
from src.services.treatment_service import TreatmentService

class TestTreatmentService:
    """Test cases for TreatmentService"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.service = TreatmentService()
    
    def test_service_initialization(self):
        """Test service initialization"""
        assert self.service is not None
        assert isinstance(self.service, TreatmentService)
    
    def test_treatments_loaded(self):
        """Test that treatments are properly loaded"""
        assert len(self.service.treatments) == 9
        assert 'Neck_Blast' in self.service.treatments
        assert 'Healthy Rice Leaf' in self.service.treatments
    
    def test_get_treatment_valid_disease(self):
        """Test getting treatment for valid disease"""
        treatment = self.service.get_treatment('Neck_Blast')
        assert treatment is not None
        assert 'Neck Blast' in treatment
        assert 'গোড়ার দাগ রোগ' in treatment
    
    def test_get_treatment_invalid_disease(self):
        """Test getting treatment for invalid disease"""
        treatment = self.service.get_treatment('Invalid Disease')
        assert "Unknown disease" in treatment
    
    def test_treatment_structure(self):
        """Test that treatment has required structure"""
        treatment = self.service.treatments['Neck_Blast']
        required_keys = ['title', 'cause', 'symptoms', 'biological_control', 'chemical_control']
        
        for key in required_keys:
            assert key in treatment
            assert isinstance(treatment[key], (str, list))
    
    def test_all_diseases_have_treatments(self):
        """Test that all diseases have treatment information"""
        for disease_name in self.service.treatments.keys():
            treatment = self.service.get_treatment(disease_name)
            assert treatment is not None
            assert len(treatment) > 0
