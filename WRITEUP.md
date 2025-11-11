# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

_For **both** a VM or App Service solution for the CMS app:_

## Virtual Machine (VM) Analysis:

**Costs:**

- Higher monthly costs due to need for dedicated compute resources 24/7
- Additional costs for OS licensing, storage, and network resources
- Requires manual management of patching, updates, and maintenance

**Scalability:**

- Manual scaling - requires creating additional VMs and load balancers
- More complex auto-scaling setup
- Limited by VM size constraints

**Availability:**

- Requires manual setup of high availability with multiple VMs
- Need to configure load balancers and availability sets
- More prone to single points of failure

**Workflow:**

- Full control over the environment and OS
- Complex deployment and maintenance
- Requires server administration expertise

## App Service Analysis:

**Costs:**

- Pay-per-use pricing model with automatic scaling
- No OS licensing costs
- Built-in management features reduce operational overhead

**Scalability:**

- Automatic scaling based on metrics
- Easy vertical and horizontal scaling
- Built-in load balancing

**Availability:**

- Built-in high availability and SLA guarantees
- Automatic failover capabilities
- Multiple deployment slots for zero-downtime deployments

**Workflow:**

- Simplified deployment through Git integration or CI/CD pipelines
- Managed platform with automatic updates
- Focus on application code rather than infrastructure

## Choice: App Service

**Justification:**
I choose App Service for this Flask CMS application because:

1. **Cost Efficiency**: For a small to medium-scale CMS application, App Service provides better cost optimization with its pay-as-you-scale model
2. **Simplicity**: The managed platform reduces operational complexity, allowing focus on application development
3. **Built-in Features**: Integrated logging, monitoring, and deployment capabilities align perfectly with project requirements
4. **Automatic Management**: Platform handles OS updates, security patches, and infrastructure maintenance
5. **Quick Deployment**: Faster time to market with streamlined deployment processes

### Assess app changes that would change your decision.

**Scenarios that would favor VM over App Service:**

1. **Custom Software Requirements**: If the application required specific software, drivers, or services not available in App Service runtime
2. **Legacy Dependencies**: Applications with legacy components requiring specific OS configurations or older runtime versions
3. **Intensive Compute Workloads**: CPU or memory-intensive operations that exceed App Service limitations
4. **Network Isolation**: Requirements for custom network configurations, VPNs, or strict network security policies
5. **File System Access**: Need for extensive file system access, custom storage configurations, or specific directory structures
6. **Compliance Requirements**: Regulatory requirements demanding full control over the underlying infrastructure
7. **Multi-Application Hosting**: Need to host multiple different applications or services on the same infrastructure
8. **Custom Protocols**: Applications using non-HTTP protocols or requiring custom ports and networking configurations

The current Flask CMS application is well-suited for App Service as it uses standard Python/Flask stack, connects to managed Azure services (SQL Database, Blob Storage), and follows typical web application patterns.
