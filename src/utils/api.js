export async function fetchTrackData() {
  try {
    const response = await fetch('/api/track');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Failed to fetch track data:', error);
    return [];
  }
}
