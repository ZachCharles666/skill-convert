import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export interface ConversionRequest {
  source_content: string;
  source_platform: string;
  target_platform: string;
  user_email?: string;
}

export interface ConversionResponse {
  converted_content: string;
  conversion_notes: string[];
  warnings: string[];
  incompatible_features: string[];
  confidence_score: number;
}

export const convertSkill = async (
  request: ConversionRequest
): Promise<ConversionResponse> => {
  const response = await axios.post(`${API_BASE_URL}/convert`, request);
  return response.data;
};

export const uploadAndConvert = async (
  file: File,
  sourcePlatform: string,
  targetPlatform: string,
  userEmail?: string
): Promise<ConversionResponse> => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('source_platform', sourcePlatform);
  formData.append('target_platform', targetPlatform);
  if (userEmail) formData.append('user_email', userEmail);

  const response = await axios.post(`${API_BASE_URL}/upload-convert`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  });
  return response.data;
};
