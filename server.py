import httpx
from fastmcp import FastMCP

# Initialize the Protocol
mcp = FastMCP(name="Clawathon Intelligence Feed")

BASE_URL = "https://clawathon.com/api/active-missions.json"

@mcp.tool
def get_global_intel() -> str:
    """
    Primary Directive: Fetches the full list of active AI Agent Hackathons.
    Use this to survey the landscape of available bounties and missions.
    Returns: JSON string of all active and legacy missions.
    """
    try:
        with httpx.Client() as client:
            response = client.get(BASE_URL, timeout=10.0)
            response.raise_for_status()
            return response.text
    except Exception as e:
        return f"/// ERROR: CONNECTION_FAILED_TO_CLAWATHON_MAINNET: {str(e)}"

@mcp.tool
def filter_missions_by_chain(chain: str) -> str:
    """
    Tactical Filter: Isolates missions specific to a blockchain network.
    Args: chain (e.g., 'SOLANA', 'SUI', 'BASE', 'BITCOIN')
    Returns: JSON string of filtered missions.
    """
    try:
        with httpx.Client() as client:
            data = client.get(BASE_URL, timeout=10.0).json()
            
        # Normalizing input to uppercase for robust matching
        target_chain = chain.upper().strip()
        
        active = [m for m in data.get("active_missions", []) if m.get("chain") == target_chain]
        
        if not active:
            return f"/// STATUS: NO_ACTIVE_MISSIONS_DETECTED_ON_{target_chain}"
            
        return str(active)
    except Exception as e:
        return f"/// ERROR: FILTER_PROTOCOL_FAILED: {str(e)}"

@mcp.tool
def get_bounty_volume() -> str:
    """
    Economic Analysis: Calculates the total USD value of all active bounties.
    Useful for agents determining economic viability of participation.
    """
    try:
        with httpx.Client() as client:
            data = client.get(BASE_URL).json()
            
        total_usd = sum(m.get("bounty_total", 0) for m in data.get("active_missions", []))
        
        return f"/// TOTAL_AVAILABLE_BOUNTY_VOLUME: ${total_usd:,} USD"
    except Exception:
        return "/// ERROR: UNABLE_TO_CALCULATE_VOLUME"

if __name__ == "__main__":
    mcp.run()
